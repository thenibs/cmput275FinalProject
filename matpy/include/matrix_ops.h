/*
# Name: Ahmad Amin, Yash Bhandari & Nibras Alam
# ID: 1623338, 1616539 & 1617818
# CMPUT 275, Winter 2020
#
# Final Project
#
# Consulted C++ Documentation; Consulted Wikipedia for Strassen
#
# File contains headers for non-trivial Matrix operations
*/

#pragma once
#include "matrix.h"

// function pointer for binary operation
typedef Matrix *(*binaryOp)(Matrix const *, Matrix const *);

/**
 * Uses a naive O(N^3) algorithm to calculate the matrix product AB.
 * Precondition: A and B are of the correct dimension
 */
Matrix *naiveMult(Matrix const *A, Matrix const *B);

// Main recursive function for Strassen algorithm
void strassenRecur(Matrix const *A, Matrix const *B, Matrix *C, size_t n);

/**
 * Uses the Strassen algorithm to multiply matrices in O(~N^2.8074).
 * Recursive approach based on Wikipedia page algorithm description and
    C source code. Designed for this library and extended to work with
    any valid matrix multiplication
 * Precondition: A and B are of the correct dimension
 */
Matrix *strassenMult(Matrix const *A, Matrix const *B);

binaryOp optimalMultAlgorithm(Matrix const *A, Matrix const *B);
