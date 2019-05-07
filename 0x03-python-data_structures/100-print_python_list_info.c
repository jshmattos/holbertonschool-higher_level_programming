#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints info about a python list
 * @p: pointer to PyObject struct
 */
void print_python_list_info(PyObject *p)
{
	register int i;
	long int len = PyList_Size(p);
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", len);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < len; i++)
	{
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
	}
}
