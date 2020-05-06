.PHONY: AllFiles
.PHONY: main.py
.PHONY: DebugPy
.PHONY: InstallPyLint

InstallPyLint:
	pip3 install pylint

AllFiles: main.py

main.py:
	python3 main.py

DebugPy:
	pylint $(PATH)