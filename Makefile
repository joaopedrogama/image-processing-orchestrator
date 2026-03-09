.PHONY: install install-hooks runserver lint format

docker_run_base_command := docker compose exec
container_name := orchestrator

install-hooks:
	pre-commit install

test:
	$(docker_run_base_command) $(container_name) python manage.py test

run:
	$(docker_run_base_command) $(container_name) python manage.py runserver
