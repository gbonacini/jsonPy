bin_PROGRAMS = jsonPy.so$(EXEEXT)

jsonPy.pym:  ../src/jsonPy.pym
	cp ../src/jsonPy.pym .

jsonPy.c: ../src/jsonPy.c
	cp ../src/jsonPy.c .

jsonPy.so$(EXEEXT): jsonPy.pym jsonPy.c
	python $(PYCFLAGS) $(AM_PYCFLAGS)  jsonPy.pym build_ext -Llibs/ -I./include/:../include ;  cp $$(find . -name "jsonPy.o") .; cp $$(find . -name "jsonPy.so") .

test: jsonPy.pym jsonPy.c
if OSX
		DYLD_LIBRARY_PATH=./libs/ python test.py
		DYLD_LIBRARY_PATH=./libs/ python test2.py
		DYLD_LIBRARY_PATH=./libs/ python test3.py
		DYLD_LIBRARY_PATH=./libs/ python test4.py
endif
if LINUX
		LD_LIBRARY_PATH=./libs/ python test.py
		LD_LIBRARY_PATH=./libs/ python test2.py
		LD_LIBRARY_PATH=./libs/ python test3.py
		LD_LIBRARY_PATH=./libs/ python test4.py
endif

PHONY: test

clean-local:
	-rm -rf build jsonPy.c  jsonPy.pym *xml
