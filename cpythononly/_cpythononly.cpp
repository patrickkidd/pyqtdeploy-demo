#include "_cpythononly.h"


PyObject *from_cpython(PyObject *pyBytes) {
    char *ro_buffer;
    Py_ssize_t length;
    if(PyBytes_AsStringAndSize(pyBytes, &ro_buffer, &length) == -1) {
        PyTypeObject* type = pyBytes->ob_type;
        std::cout << "Expected python buffer object, got " << type->tp_name << std::endl;
        return NULL;
    }

    return PyUnicode_FromStringAndSize(ro_buffer, length);
}
