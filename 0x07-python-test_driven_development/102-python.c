#include <Python.h>
#include <object.h>
#include <bytesobject.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * print_python_string - prints Python strings
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t length;
	wchar_t *value;
	char *dataType;

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("ERROR] Invalid String Object\n");
		return;
	}
	length = ((PyASCIIObject *)(p))->length;
	value = PyUnicode_AsWideCharString(p, &length);
	dataType = PyUnicode_IS_COMPACT_ASCII(p)
		? "compact ascii"
		: "compact unicode object";
	printf("  type: %s\n", dataType);
	printf("  length: %lu\n", length);
	printf("  value: %ls\n", value);
}
