# Makefile etl-notebooks
# Makefile pyne-workshop-scraping-web

.PHONY: all help clean pep8 check.test_path

clean: clean-build clean-others clean-pyc clean-test

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr .eggs/
	@find . -name '*.egg-info' -exec rm -fr {} +
	@find . -name '*.egg' -exec rm -f {} +

clean-others:
	@find . -name 'Thumbs.db' -exec rm -f {} \;

clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	@rm -fr .tox/
	@rm -f .coverage
	@rm -fr htmlcov/

pep8:
	@pycodestyle --filename="*.py" .

check.test_path:
	@if test "$(TEST_PATH)" = "" ; then echo "TEST_PATH is undefined. The default is tests."; fi

test: check.test_path
	@py.test $(TEST_PATH) --cov --cov-report term-missing --basetemp=tests/media --disable-pytest-warnings

test.failfirst: check.test_path
	@py.test -x $(TEST_PATH) --cov-report term-missing --basetemp=tests/media --disable-pytest-warnings

test.collect: check.test_path
	@py.test $(TEST_PATH) --collect-only --disable-pytest-warnings
