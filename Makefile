.PHONY: AllPyFiles
.PHONY: main.py
.PHONY: CFILTER

AllPyFiles:
	main.py

main.py:
	python3 main.py

# Not needed, but just in case we want some C backend!
CFILTER:
	gcc -g   -o main.o main.c
	clear
	./main.o