

.phony: all

all:
	python collect.py A > output/a-klass.md
	python collect.py B > output/b-klass.md
	python collect.py D > output/d-klass.md
