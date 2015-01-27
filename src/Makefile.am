bin_PROGRAMS = jsonPy.so$(EXEEXT)

jsonPy.so$(EXEEXT): jsonPy.pym jsonPy.c
	python $(PYCFLAGS) $(AM_PYCFLAGS)  jsonPy.pym build_ext -I../include/ ; cp $$(find . -name "jsonPy.o") .; cp $$(find . -name "jsonPy.so") .

install-data-hook:
	python $(PYCFLAGS) $(AM_PYCFLAGS)  jsonPy.pym install

clean-local:
	-rm -rf build
