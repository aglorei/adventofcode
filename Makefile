PYLINT = pipenv run pylint
PYLINTFLAGS = -rn --rcfile .pylintrc

SOURCES := $(wildcard 2018/**/*.py)

pylint: $(patsubst %.py,%.pylint,$(SOURCES))

%.pylint:
	$(PYLINT) $(PYLINTFLAGS) $*.py
