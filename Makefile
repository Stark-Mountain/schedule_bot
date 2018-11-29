.PHONY: clear
clear:
	find . -name '*.pyc' -delete

.PHONY: testcov
testcov:
	pytest --cov=src && (echo "building coverage html, view at './htmlcov/index.html'"; coverage html)

.PHONY: runtest
test:
	docker build -t schedulebot_test -f Dockerfile.testing .
	docker run schedulebot_test

.PHONY: test
test: clear runtest

.PHONY: reset-database
reset-database:
	python -c "from src.management import prepare_database; prepare_database(True)"

.PHONY: run
run:
	docker build -t schedulebot .
	docker-compose -f docker-compose.yaml up --force-recreate

.PHONY: deploy
deploy:
	docker build --build-arg requirements_file=prod.txt -t schedulebot_prod .
	docker-compose -f production.yaml up -d

.PHONY: stop
stop:
	docker-compose -f production.yaml stop

.PHONY: psql
psql:
	psql -U schedulebot -p 5432 -h localhost
