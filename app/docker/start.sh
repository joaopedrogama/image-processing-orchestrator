#!/usr/bin/env bash

set -e

if ! [ -z "$LOGS_ROOT" ]; then
    mkdir -p "$LOGS_ROOT"
fi

if ! [ -z "$STATIC_ROOT" ]; then
    mkdir -p "$STATIC_ROOT"
fi

if ! [ -z "$MEDIA_ROOT" ]; then
    mkdir -p "$MEDIA_ROOT"
fi

until PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -d "$POSTGRES_DATABASE" -c "\q" 1>/dev/null 2>&1; do
    echo "Postgres is unavailable, waiting..."
    sleep 5
done

if [ "$MODE" = "development" ]; then
    echo "Creating migrations..."
    python manage.py makemigrations --noinput
    echo "Finished creating migrations"
fi

echo "Applying migrations..."
python manage.py migrate
echo "Migrations applied"

if [ "$MODE" != "development" ]; then
    echo "Copying default media..."
    mkdir -p "/var/www/orchestrator/media/"
    if [ -d "/usr/src/app/main/media/" ]; then
        cp -a "/usr/src/app/main/media/." "/var/www/orchestrator/media/"
    fi
    echo "Finished copying default media"

    echo "Collecting static files..."
    python manage.py collectstatic --clear --noinput -v 0
    echo "Finished collecting static files"
fi

echo "Starting Memcache..."
mkdir -p "/var/run/orchestrator"
memcached -a 0700 -u root \
    -s "/var/run/orchestrator/memcached.sock" \
    1>>"$LOGS_ROOT/memcached.log" 2>&1 &
echo "Memcache started"

echo "Starting Orchestrator as `whoami`"
if [ "$MODE" = "development" ]; then
    python -m uvicorn config.asgi:application --reload --host 0.0.0.0 --port 8000
else
    exec gunicorn "config.asgi:application" \
        --name "orchestrator" \
        --bind "0.0.0.0:8000" \
        --workers "$NUM_GUNICORN_WORKERS" \
        --worker-class uvicorn.workers.UvicornWorker \
        --timeout "300" \
        --log-level "INFO" \
        --log-file "$LOGS_ROOT/gunicorn_info.log" \
        --access-logfile "$LOGS_ROOT/gunicorn_access.log"
fi
