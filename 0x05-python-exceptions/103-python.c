#include <Python.h>
#include <object.h>

void print_python_float(PyObject *p)
{
	float f = 0;
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	f = PyFloat_AsDouble(p);
	printf("  value: %1g\n", f);
}

/**
 * print_python_bytes - print some basic info about Pyton
 * byte objects
 * @p: pointer to PyObject p
 */
void print_python_bytes(PyObject *p)
{
	register int i;
	ssize_t bytes;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	PyBytes_AsStringAndSize(p, &str, &bytes);
	printf("  size: %li\n", bytes);
	printf("  trying string: %s\n", str);
	if (bytes > 10)
		bytes = 10;
	else
		bytes++;
	printf("  first %li bytes: ", bytes);
	for (i = 0; i < bytes - 1; i++)
		printf("%02hhx ", str[i]);
	printf("%02hhx", str[i]);
	printf("\n");
}

/**
 * print_python_list - print some basic info about Python lists
 * @p: pointer to PyObject p
 */
void print_python_list(PyObject *p)
{
	register int i, size, allocated;
	const char *dataType;
	PyListObject *list = (PyListObject *)p;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	/* can't use */
	size = PyList_GET_SIZE(p);
	allocated = list->allocated;

	printf("[*] Size of the Python List = %i\n", size);
	printf("[*] Allocated = %i\n", allocated);
	for (i = 0; i < size; i++)
	{
		dataType = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %i: %s\n", i, dataType);
		if (strcmp(dataType, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		if (strcmp(dataType, "float") == 0)
			print_python_float(list->ob_item[i]);
	}
}

