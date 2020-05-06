.PHONY: AllFiles
.PHONY: main.py
.PHONY: DebugPy
.PHONY: InstallPyLint

InstallPyLint:
	apt-get install pylint

AllFiles: main.py

main.py:
	python3 main.py

DebugPy:
	pylint $(PATH)