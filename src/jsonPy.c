#include <jsonPy.h>

int _open(char const *filePath){
	int result=0;
	errno=0;
	result=parseJsonConfig(filePath, &nodeRoot, &fullIndexesList);
	if(result>0){
		return result;
	}else{
		errno=EINVAL;
		return 0;
	}
}

char* _getStringValueByPath(char const *url){
	node* tempNode;
	errno=0;
	pathIndex* element = getElementValueByString(fullIndexesList, url);
	if(element!=NULL){
		tempNode=element->Node;
		if(tempNode->nodeType == TEXT_T){
			return((tempNode->data).string);
		}
	}
	errno=EINVAL;
	return NULL;
}

double _getNumericValueByPath(char const *url){
	node* tempNode;
	errno=0;
	pathIndex* element = getElementValueByString(fullIndexesList, url);
	if(element!=NULL){
		tempNode=element->Node;
		if(tempNode->nodeType == NUMERIC_T){
			return((tempNode->data).number);
		}
	}
	errno=EINVAL;
	return 0.0;
}

bool _getBoolValueByPath(char const *url){
	node* tempNode;
	errno=0;
	pathIndex* element = getElementValueByString(fullIndexesList, url);
	if(element!=NULL){
		tempNode=element->Node;
		if(tempNode->nodeType == BOOL_T){
			return((tempNode->data).boolean);
		}
	}
	errno=EINVAL;
	return false;
}
bool _isString(char const *url){
	node* tempNode;
	errno=0;
	pathIndex* element = getElementValueByString(fullIndexesList, url);
	if(element!=NULL){
		tempNode=element->Node;
		if(tempNode->nodeType == TEXT_T){
			return true;
		}
	}else{
		errno=EINVAL;
	}
	return false;
}
bool _isNumber(char const *url){
	node* tempNode;
	errno=0;
	pathIndex* element = getElementValueByString(fullIndexesList, url);
	if(element!=NULL){
		tempNode=element->Node;
		if(tempNode->nodeType == NUMERIC_T){
			return true;
		}
	}else{
		errno=EINVAL;
	}
	return false;
}
bool _isBoolean(char const *url){
	node* tempNode;
	errno=0;
	pathIndex* element = getElementValueByString(fullIndexesList, url);
	if(element!=NULL){
		tempNode=element->Node;
		if(tempNode->nodeType == BOOL_T){
			return true;
		}
	}else{
		errno=EINVAL;
	}
	return false;
}
bool _isValid(char const *url){
	pathIndex* element = getElementValueByString(fullIndexesList, url);
	if(element!=NULL){
			return true;
	}
	return false;
}
static PyObject *isString(PyObject* self, PyObject* args){
	char const *url;
	bool result=false;

	if (!PyArg_ParseTuple(args, "s", &url))
		return NULL;

	result=_isString(url);
	if(errno==0){
		return Py_BuildValue("i", result);
	}else{
		PyErr_SetString(JsonPyError, "Invalid Json node");
		return NULL;
	}
}

static PyObject *isNumber(PyObject* self, PyObject* args){
	char const *url;
	bool result=false;

	if (!PyArg_ParseTuple(args, "s", &url))
		return NULL;

	result=_isNumber(url);
	if(errno==0){
		return Py_BuildValue("i", result);
	}else{
		PyErr_SetString(JsonPyError, "Invalid Json node");
		return NULL;
	}
	return NULL;
}
static PyObject *isBoolean(PyObject* self, PyObject* args){
	char const *url;
	bool result=false;

	if (!PyArg_ParseTuple(args, "s", &url))
		return NULL;

	result=_isBoolean(url);
	if(errno==0){
		return Py_BuildValue("i", result);
	}else{
		PyErr_SetString(JsonPyError, "Invalid Json node");
		return NULL;
	}
	return NULL;
}
static PyObject *isValid(PyObject* self, PyObject* args){
	char const *url;
	bool result=false;

	if (!PyArg_ParseTuple(args, "s", &url))
		return NULL;

	result=_isValid(url);
	if(errno==0){
		return Py_BuildValue("i", result);
	}else{
		PyErr_SetString(JsonPyError, "Invalid Json node");
		return NULL;
	}
}

static PyObject *open(PyObject* self, PyObject* args){
	char const *filePath;
	int result=0;
	errno=0;

	if (!PyArg_ParseTuple(args, "s", &filePath))
		return NULL;
	result=_open(filePath);
	if(errno==0){
		return Py_BuildValue("i", result);
	}else{
		PyErr_SetString(JsonPyError, "Invalid Json file");
		return NULL;
	}
}

static PyObject *getStringValueByPath(PyObject* self, PyObject* args){
	char const *url;
	char* result=NULL;

	if (!PyArg_ParseTuple(args, "s", &url))
		return NULL;

	result=_getStringValueByPath(url);
	if(errno==0){
		return Py_BuildValue("s", result);
	}else{
		PyErr_SetString(JsonPyError, "Invalid Json node");
		return NULL;
	}
}

static PyObject *getNumericValueByPath(PyObject* self, PyObject* args){
	char const *url;
	double result=0.0;

	if (!PyArg_ParseTuple(args, "s", &url))
		return NULL;
	result=_getNumericValueByPath(url);
	if(errno==0){
		return Py_BuildValue("d", result);
	}else{
		PyErr_SetString(JsonPyError, "Invalid Json node");
		return NULL;
	}
}

static PyObject *getBoolValueByPath(PyObject* self, PyObject* args){
	char const *url;
	bool result=false;

	if (!PyArg_ParseTuple(args, "s", &url))
		return NULL;
	result=_getBoolValueByPath(url);
	if(errno==0){
		return Py_BuildValue("i", result);
	}else{
		PyErr_SetString(JsonPyError, "Invalid Json node");
		return NULL;
	}
}

PyMODINIT_FUNC
initjsonPy(void){
	PyObject *m = Py_InitModule3("jsonPy", JsonPY, module_docstring);
	if (m == NULL)
		return;
	JsonPyError = PyErr_NewException("jsonPy.JsonPyError", NULL, NULL);
	Py_INCREF(JsonPyError);
	PyModule_AddObject(m, "JsonPyError", JsonPyError);
}
