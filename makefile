all: test.py crab.py
	python crab.py
	python test.py

clean:
	rm -r -f *.png *.ppm
