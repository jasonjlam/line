all: test.py crab.py
	python crab.py
	python test.py
	@echo Crab is in crabRave.ppm, test image is in test.ppm
clean:
	rm -r -f *.png *.ppm
