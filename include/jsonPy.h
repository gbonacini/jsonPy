#ifndef __JSONPY_H__
#define  __JSONPY_H__

#include <config.h>

#ifdef HAVE_STDBOOL_H
#include <stdbool.h>
#endif

#include <Python.h>
#include <parseJsonConfig.h>
#include <sys/errno.h>

static PyObject *JsonPyError;

static char module_docstring[] = "This module provides an interface to the parseJsonLY C library.";
static char open_docstring[] = "Open and parse a JSON configuration file using the parseJsonLY C library.";
static char getStringValueByPath_docstring[] = "Return a string value of a JSON element or an exception using a string with the 'url'.";
static char getNumericValueByPath_docstring[] = "Return a numeric value of a JSON element or an exception using a string with the 'url'.";
static char getBoolValueByPath_docstring[] = "Return a boolean value of a JSON element or an exception using a string with the 'url'.";
static char isString_docstring[] = "Return a boolean value: true if the JSON element is a string, false in the negative case.";
static char isNumber_docstring[] = "Return a boolean value: true if the JSON element is a string, false in the negative case.";
static char isBoolean_docstring[] = "Return a boolean value: true if the JSON element is a string, false in the negative case.";
static char isValid_docstring[] = "Return a boolean value: true if the JSON element is present, false in the negative case.";

extern int errno;
node nodeRoot;
pathIndex* fullIndexesList;

int _open(char const *filePath);
char* _getStringValueByPath(char const *url);
double _getNumericValueByPath(char const *url);
bool _getBoolValueByPath(char const *url);
static PyObject *open(PyObject *self, PyObject *args);
static PyObject *getStringValueByPath(PyObject* self, PyObject* args);
static PyObject *getNumericValueByPath(PyObject* self, PyObject* args);
static PyObject *getBoolValueByPath(PyObject* self, PyObject* args);
static PyObject *isString(PyObject* self, PyObject* args);
static PyObject *isNumber(PyObject* self, PyObject* args);
static PyObject *isBoolean(PyObject* self, PyObject* args);
static PyObject *isValid(PyObject* self, PyObject* args);

static PyMethodDef JsonPY[] = {
	{"open", open, METH_VARARGS, open_docstring},
	{"getStringValueByPath", getStringValueByPath, METH_VARARGS, getStringValueByPath_docstring},
	{"getNumericValueByPath", getNumericValueByPath, METH_VARARGS, getNumericValueByPath_docstring},
	{"getBoolValueByPath", getBoolValueByPath, METH_VARARGS, getBoolValueByPath_docstring},
	{"isString", isString, METH_VARARGS, isString_docstring},
	{"isNumber", isNumber, METH_VARARGS, isNumber_docstring},
	{"isBoolean", isBoolean, METH_VARARGS, isBoolean_docstring},
	{"isValid", isValid, METH_VARARGS, isValid_docstring},
	{NULL, NULL, 0, NULL}
};

#endif
