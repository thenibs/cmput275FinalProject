/*
# Name: Ahmad Amin, Yash Bhandari & Nibras Alam
# ID: 1623338, 1616539 & 1617818
# CMPUT 275, Winter 2020
#
# Final Project
#
# Consulted C++ Documentation;
*/
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "matrix.h"
#include "matrix_ops.h"

namespace py = pybind11;

PYBIND11_MODULE(matpy, m)
{
    m.doc() = "A matrix arithmetic library";

    py::class_<Matrix>(m, "Matrix")
        .def(py::init<size_t, size_t, int>())
        .def(py::init<std::vector<std::vector<int>>>())
        .def("get", &Matrix::get)
        .def("set", &Matrix::set)
        .def("add", &Matrix::add)
        .def("mult", &Matrix::mult)
        .def("scale", &Matrix::scale)
        .def("str", &Matrix::str)
        .def("dim", &Matrix::dim)
        .def("equals", &Matrix::equals)
        .def("exp", &Matrix::exp)
        .def_static("id", &Matrix::id)
        .def_static("naive_mult", &naiveMult)
        .def_static("strassen_mult", &strassenMult);
}
