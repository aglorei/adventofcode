install:
	pipenv sync

lint:
	pipenv run pylint --rcfile .pylintrc 2018
