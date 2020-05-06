.PHONY: AllFiles
.PHONY: main.py
.PHONY: DebugPy

AllFiles: main.py

main.py:
	python3 main.py

DebugPy:
	pylint $(PATH)