#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list - print some basic info about Python lists
 * @p: pointer to PyObject p
 */
void print_python_list(PyObject *p)
{
	(void)p;
	return;
}

/**
 * print_python_bytes - print some basic info about Pyton
 * byte objects
 * @p: pointer to PyObject p
 */
void print_python_bytes(PyObject *p)
{
	register int i, bytes;
	PyBytesObject *b = (PyBytesObject *)p;

	bytes = PyBytes_Size(p);

	if (!p || !b)
		printf("[ERROR] Invalid Bytes Object\n");
	printf("[.] bytes object info\n");
	printf("  size: %i\n", bytes);
	printf("  trying string: %s\n", PyBytes_AsString(p));
	if (bytes > 10)
		bytes = 10;
	else
		bytes++;
	printf("  first %i bytes: ", bytes);
	for (i = 0; i < bytes; i++)
	{
		printf("%i ", 14);
	}
	printf("\n");
}

