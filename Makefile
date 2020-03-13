build :
	rm -r env
	python3 -m venv env
	. env/bin/activate && pip install -r requirements.txt

test:
	. env/bin/activate && python -m pytest -ra
