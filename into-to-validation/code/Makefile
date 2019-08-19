a.out: abs.c
	gcc abs.c

env: requirements.txt
	python3 -m venv env
	. env/bin/activate && pip3 install -r requirements.txt
