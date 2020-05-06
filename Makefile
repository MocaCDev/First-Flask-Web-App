.PHONY: AllFiles
.PHONY: main.py
.PHONY: DebugPy
.PHONY: InstallFlake8

make foo=bar target

InstallFlake8:
	python -m pip3 install flake8

AllFiles: main.py

main.py:
	python3 main.py

DebugPy:
	flake8 $(foo)