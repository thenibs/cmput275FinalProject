/*
# Name: Ahmad Amin, Yash Bhandari & Nibras Alam
# ID: 1623338, 1616539 & 1617818
# CMPUT 275, Winter 2020
#
# Final Project
#
# Consulted C++ Documentation;
*/
#pragma once
#include <string>
#include <vector>
#include <tuple>

class Matrix
{
public:
    // Checks if an input 2d list is rectangular
    static bool wellFormed(std::vector<std::vector<int>> matrixValues);
    
    // Creats an n x n identity matrix
    static Matrix *id(size_t n);
    Matrix() = delete;
    
    // Creates empty mxn matrix with values initialized to fill parameter
    Matrix(size_t m, size_t n, int fill = 0);
    
    // Creates a matrix with values from a 2d vector
    Matrix(std::vector<std::vector<int>> matrixValues);
    
    ~Matrix();
    
    // Gets the i,j-th entry of the matrix
    int get(size_t i, size_t j) const;
    
    // Sets the i,j-th entry to the given val
    void set(size_t i, size_t j, int val);
    
    // Returns the matrix sum of this matrix with the other matrix
    Matrix *add(Matrix const *other) const;
    
    // Returns the matrix product of this matrix with other matrix
    Matrix *mult(Matrix const *other) const;
    
    // Returns the scalar product of this matrix with the given scalar
    Matrix *scale(int scalar) const;
    
    // Performs element-wise equality check with other matrix
    bool equals(Matrix const *other) const;

    // Returns the matrix A^x
    Matrix *exp(unsigned int x);
    
    // Returns the string representation of the matrix
    std::string str() const;
    
    // Returns the dimension of the matrix as a tuple
    std::tuple<size_t, size_t> dim() const;
    
    // Returns the number of rows in the matrix
    size_t numRows() const;
    
    // Returns the number of columns in the matrix
    size_t numCols() const;

private:
    int *mat;
    size_t m, n;
    static std::string formatDim(std::tuple<size_t, size_t> dimension);
};
