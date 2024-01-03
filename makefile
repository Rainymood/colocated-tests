
test:
	pytest -s -v --ignore=src/entrypoint/

test-full:
	pytest -s -v

run:
	set pythonpath=src
	python src/entrypoint/cli.py 1 2

