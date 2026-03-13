.PHONY: install install-hooks runserver lint format test coverage

docker_run_base_command := docker compose exec
container_name := orchestrator

install-hooks:
	pre-commit install

test:
	$(docker_run_test_command) python manage.py test --no-input

coverage: .coverage
	$(docker_run_base_command) $(container_name) coverage report --fail-under 80 --precision 2 --sort cover

.coverage:
	$(docker_run_test_command) coverage run manage.py test --no-input || true

run:
	$(docker_run_base_command) $(container_name) python manage.py runserver

ruff:
	$(docker_run_base_command) $(container_name) ruff check .

fix:
	$(docker_run_base_command) $(container_name) ruff check --fix .

format:
	$(docker_run_base_command) $(container_name) ruff format .
