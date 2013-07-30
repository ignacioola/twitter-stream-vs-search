
install: venv
	pip install -r requirements.txt

venv:
	virtualenv --no-site-packages --distribute venv

.PHONY: install
