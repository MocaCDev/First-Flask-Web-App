.PHONY: AllFiles
.PHONY: main.py
.PHONY: DebugPy

AllFiles: main.py

main.py:
	python3 main.py

DebugPy:
	#INSTALLING PYLINT
	pip3 install pylint
	#DEBUGGING WITH PYLINT
	pylint $(PATH)