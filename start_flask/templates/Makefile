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
test:
	FLASK_ENV=test pytest tests/ -v --cov=delivery
run:
	FLASK_APP={{ proj }}/app.py flask run
run-dev:
	FLASK_APP={{ proj }}/app.py FLASK_ENV=development flask run