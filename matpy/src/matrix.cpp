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
#include <exception>
#include <iostream>
#include "matrix.h"
#include "matrix_ops.h"

namespace py = pybind11;

bool Matrix::wellFormed(std::vector<std::vector<int>> matrixValues)
{
    size_t n = matrixValues[0].size();
    for (auto row : matrixValues)
        if (row.size() != n)
            return false;
    return true;
}

Matrix *Matrix::id(size_t n)
{
    Matrix *idMat = new Matrix(n, n);
    for (size_t i = 0; i < n; i++)
    {
        idMat->set(i, i, 1);
    }
    return idMat;
}

Matrix::Matrix(size_t m, size_t n, int fill)
    : m(m), n(n)
{
    mat = new int[m * n];
    for (size_t i = 0; i < m * n; i++)
        mat[i] = fill;
}

Matrix::Matrix(std::vector<std::vector<int>> matrixValues)
{
    if (!wellFormed(matrixValues))
        throw std::invalid_argument("Matrix had rows of different lengths");

    m = matrixValues.size();
    n = matrixValues[0].size();
    mat = new int[m * n];
    for (size_t i = 0; i < m; i++)
    {
        for (size_t j = 0; j < n; j++)
        {
            mat[i * n + j] = matrixValues[i][j];
        }
    }
}

Matrix::~Matrix()
{
    delete[] mat;
}

std::string Matrix::str() const
{
    std::string result = std::to_string(m) + 'x' + std::to_string(n) + " Matrix:";
    for (size_t i = 0; i < m; i++)
    {
        result += '\n';
        for (size_t j = 0; j < n; j++)
        {
            result += std::to_string(mat[i * n + j]) + ' ';
        }
    }
    return result;
}

int Matrix::get(size_t i, size_t j) const
{
    return mat[i * n + j];
}

void Matrix::set(size_t i, size_t j, int val)
{
    mat[i * n + j] = val;
}

std::tuple<size_t, size_t> Matrix::dim() const
{
    return std::tuple<size_t, size_t>(m, n);
}

Matrix *Matrix::add(Matrix const *other) const
{
    if (dim() != other->dim())
    {
        std::string dim1 = formatDim(other->dim());
        std::string dim2 = formatDim(dim());
        throw std::invalid_argument("Matrix of dimension " + dim1 + " cannot \
                            be multiplied with matrix of dimension " +
                                    dim2);
    }

    Matrix *sum = new Matrix(m, n);
    for (size_t i = 0; i < m; i++)
    {
        for (size_t j = 0; j < n; j++)
        {
            int entry = other->get(i, j) + get(i, j);
            sum->set(i, j, entry);
        }
    }
    return sum;
}

Matrix *Matrix::mult(Matrix const *other) const
{
    if (numCols() != other->numRows())
    {
        std::string dim1 = formatDim(other->dim());
        std::string dim2 = formatDim(dim());
        throw std::invalid_argument("Matrix of dimension " + dim1 + " cannot \
                            be multiplied with matrix of dimension " +
                                    dim2);
    }

    auto multAlgorithm = optimalMultAlgorithm(this, other);
    return multAlgorithm(this, other);
}

Matrix *Matrix::scale(int scalar) const
{
    Matrix *result = new Matrix(numRows(), numCols());
    for (size_t i = 0; i < numRows(); i++)
    {
        for (size_t j = 0; j < numCols(); j++)
        {
            int scaled = scalar * get(i, j);
            result->set(i, j, scaled);
        }
    }
    return result;
}

bool Matrix::equals(Matrix const *other) const
{
    if (dim() != other->dim())
    {
        return false;
    }

    for (size_t i = 0; i < m; i++)
    {
        for (size_t j = 0; j < n; j++)
        {
            if (get(i, j) != other->get(i, j))
            {
                return false;
            }
        }
    }
    return true;
}

Matrix *Matrix::exp(unsigned int x)
{
    if (numRows() != numCols())
    {
        throw std::invalid_argument("Cannot exponentiate matrix of dimension " + formatDim(dim()) + ". Matrix must be square.");
    }
    // either return identity matrix or prepare for calculation
    Matrix *result;
    if (x == 0)
    {
        result = id(numRows());
    }
    else
    {
        // copy matrix to result matrix (A^1)
        result = new Matrix(numRows(), numCols());
        for (size_t i = 0; i < numRows(); i++)
        {
            for (size_t j = 0; j < numCols(); j++)
            {
                result->set(i, j, get(i, j));
            }
        }

        // repeatedly multiply matrix to result matrix(A^x)
        for (unsigned int i = 1; i < x; i++)
        {
            result = mult(result);
        }
    }

    return result;
}

size_t Matrix::numRows() const
{
    return m;
}

size_t Matrix::numCols() const
{
    return n;
}

std::string Matrix::formatDim(std::tuple<size_t, size_t> dimension)
{
    std::string dim1 = std::to_string(std::get<0>(dimension));
    std::string dim2 = std::to_string(std::get<1>(dimension));
    return "(" + dim1 + ", " + dim2 + ")";
}
