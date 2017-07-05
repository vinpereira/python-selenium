init:
	pip install -r requirements.txt

run_simple:
	python simple_test.py

run_class:
	python test_class.py

.PHONY: 
	clean-pyc clean-build