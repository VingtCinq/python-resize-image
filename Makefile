
all:
	@echo "Héllo, try ''make check"

check:
	py.test --cov-report=html --cov imageresize tests/tests.py -sv
