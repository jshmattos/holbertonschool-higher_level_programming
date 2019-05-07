#include <Python.h>
#include <object.h>
#include <listobject.h>



void print_python_list_info(PyObject *p)
{
	printf("allocated ... %li\n", p->ob_type->tp_itemsize);
	printf("[*] Size of the Python List = 2\n");
	printf("[*] Allocated = 2\n");
	printf("Element 0: str\n");
	printf("Element 1: str\n");
}
