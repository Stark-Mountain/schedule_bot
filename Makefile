.PHONY: test
test:
	pytest --cov=src

.PHONY: testcov
testcov:
	pytest --cov=src && (echo "building coverage html, view at './htmlcov/index.html'"; coverage html)


.PHONY: reset-database
reset-database:
	python -c "from src.management import prepare_database; prepare_database(True)"


.PHONY: run
run:
	pipenv run adev runserver
