#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <string.h>

/**
 * print_python_bytes - print some basic info about Pyton
 * byte objects
 * @p: pointer to PyObject p
 */
void print_python_bytes(PyObject *p)
{
	register int i, bytes;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	str = PyBytes_AsString(p);
	bytes = PyBytes_Size(p);
	printf("  size: %i\n", bytes);
	printf("  trying string: %s\n", str);
	if (bytes > 10)
		bytes = 10;
	else
		bytes++;
	printf("  first %i bytes: ", bytes);
	for (i = 0; i < bytes; i++)
	{
		printf("%02x ", str[i]);
	}
	printf("\n");
}

/**
 * print_python_list - print some basic info about Python lists
 * @p: pointer to PyObject p
 */
void print_python_list(PyObject *p)
{
	int i, size, allocated;
	PyListObject *list = (PyListObject *)p;

	size = PyList_Size(p);
	allocated = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %i\n", size);
	printf("[*] Allocated = %i\n", allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %i: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
		if (strcmp(Py_TYPE(list->ob_item[i])->tp_name, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}
