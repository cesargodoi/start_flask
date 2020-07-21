clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build

install:
	pip install -e .

install-dev:
	pip install -e .['dev']

run:
	FLASK_APP={{ proj }}/app.py flask run

run-dev:
	FLASK_APP={{ proj }}/app.py FLASK_ENV=development flask run

init-db:
	FLASK_APP=delivery/app.py flask create-db
	FLASK_APP=delivery/app.py flask db upgrade

test:
	FLASK_ENV=test pytest tests/ -v --cov=delivery

format:
	isort **/*.py
	black -l 79 **/*.py