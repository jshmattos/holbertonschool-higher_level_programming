#include <Python.h>
#include <object.h>

void print_python_list(PyObject *p);

void print_python_bytes(PyObject *p)
{
	int size = 0;
	ssize_t bytes;
	char *string = "test";

	printf("[.] bytes object info\n");
  	printf("size: %i\n", size);
	printf("trying string: %s\n", string);

  	printf("first 6 bytes: 48 65 6c 6c 6f 00
}
void print_python_float(PyObject *p);
