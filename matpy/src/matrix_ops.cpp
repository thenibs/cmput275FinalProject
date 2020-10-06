/*
# Name: Ahmad Amin, Yash Bhandari & Nibras Alam
# ID: 1623338, 1616539 & 1617818
# CMPUT 275, Winter 2020
#
# Final Project
#
# Consulted C++ Documentation;
*/
#include "matrix_ops.h"
#include <cmath>
#include <iostream>

Matrix *naiveMult(Matrix const *A, Matrix const *B)
{
    size_t aRows = A->numRows();
    size_t aCols = A->numCols();
    size_t bCols = B->numCols();

    Matrix *prod = new Matrix(aRows, bCols);

    for (size_t i = 0; i < aRows; i++)
    {
        for (size_t j = 0; j < bCols; j++)
        {
            int result = 0;
            for (size_t k = 0; k < aCols; k++)
            {
                result += A->get(i, k) * B->get(k, j);
            }
            prod->set(i, j, result);
        }
    }
    return prod;
}

void strassenRecur(Matrix const *A, Matrix const *B, Matrix *C, size_t s)
{
    // base case if 1x1 matrices
    if (s <= 1)
    {
        C->set(0, 0, (A->get(0, 0) * B->get(0, 0)));
    }
    else
    {
        s *= 0.5;
        // creates quadrants for each of C = AxB and intermediate products
        Matrix a = Matrix(s,s), b = Matrix(s,s), c = Matrix(s,s),
            d = Matrix(s,s), e = Matrix(s,s), f = Matrix(s,s),
            g = Matrix(s,s), h = Matrix(s,s), i = Matrix(s,s),
            j = Matrix(s,s), k = Matrix(s,s), l = Matrix(s,s),
            p1 = Matrix(s,s), p2 = Matrix(s,s), p3 = Matrix(s,s),
            p4 = Matrix(s,s), p5 = Matrix(s,s), p6 = Matrix(s,s),
            p7 = Matrix(s,s);

        // pointers due to nature of Matrix library functions
        Matrix *a11 = &a, *a12 = &b, *a21 = &c, *a22 = &d,
            *b11 = &e, *b12 = &f, *b21 = &g, *b22 = &h,
            *c11 = &i, *c12 = &j, *c21 = &k, *c22 = &l,
            *m1 = &p1, *m2 = &p2, *m3 = &p3, *m4 = &p4, 
                            *m5 = &p5, *m6 = &p6, *m7 = &p7;

        // split A, B matrices into quadrants
        for (size_t i = 0; i < s; i++)
        {
            for (size_t j = 0; j < s; j++)
            {
                a11->set(i, j, A->get(i, j));
                a12->set(i, j, A->get(i, j+s));
                a21->set(i, j, A->get(i+s, j));
                a22->set(i, j, A->get(i+s, j+s));

                b11->set(i, j, B->get(i, j));
                b12->set(i, j, B->get(i, j+s));
                b21->set(i, j, B->get(i+s, j));
                b22->set(i, j, B->get(i+s, j+s));
            }
        }

        // computing the 7 products (main Strassen concept)
        strassenRecur((a11->add(a22)), (b11->add(b22)), m1, s);
        strassenRecur((a21->add(a22)), b11, m2, s);
        strassenRecur(a11, (b12->add(b22->scale(-1))), m3, s);
        strassenRecur(a22, (b21->add(b11->scale(-1))), m4, s);
        strassenRecur((a11->add(a12)), b22, m5, s);
        strassenRecur((a21->add(a11->scale(-1))), (b11->add(b12)), m6, s);
        strassenRecur((a12->add(a22->scale(-1))), (b21->add(b22)), m7, s);

        // populating the new matrix quadrants (main Strassen concept)
        c11 = m1->add(m4->add(m7->add(m5->scale(-1))));
        c12 = m3->add(m5);
        c21 = m2->add(m4);
        c22 = m1->add(m3->add(m6->add(m2->scale(-1))));

        // populating the final matrix
        for (size_t i = 0; i < s; i++)
        {
            for (size_t j = 0; j < s; j++)
            {
                C->set(i, j, c11->get(i, j));
                C->set(i, j+s, c12->get(i, j));
                C->set(i+s, j, c21->get(i, j));
                C->set(i+s, j+s, c22->get(i, j));
            }
        }
    }
}

/*
    The algorithm recursively divides matrices A and B into 4 quadrants
    to carry out only 7 multiplications vs. the typical 8.
    It requires an nxn matrix where n is a power of 2, so extra 0 padding
    is added if necessary after the optimal/minimum size is determined.
*/
Matrix *strassenMult(Matrix const *A, Matrix const *B)
{
    size_t aRows = A->numRows();
    size_t aCols = A->numCols();
    size_t bRows = B->numRows();
    size_t bCols = B->numCols();

    // larger output matrix dimension's next power of 2 = Strassen Size
    size_t s;
    if (aRows >= bCols)
    {
        s = pow(2, ceil(log(aRows)/log(2)));
    }
    else if (aRows < bCols)
    {
        s = pow(2, ceil(log(bCols)/log(2)));
    }
     
    // copies A and B into Matrices of determined Strassen Size
    Matrix a = Matrix(s,s,0), b = Matrix(s,s,0), c = Matrix(s,s,0);
    Matrix *aTemp = &a, *bTemp = &b, *output = &c;
    for (size_t i = 0; i < aRows; i++)
    {
        for (size_t j = 0; j < aCols; j++)
        {
            aTemp->set(i, j, A->get(i, j));
        }
    }

    for (size_t i = 0; i < bRows; i++)
    {
        for (size_t j = 0; j < bCols; j++)
        {
            bTemp->set(i, j, B->get(i, j));
        }
    }

    // calls on recursive function where output is passed by pointer
    strassenRecur(aTemp, bTemp, output, s);

    // copies mxn portion from output into final matrix to return
    Matrix *prod = new Matrix(aRows, bCols);
    for (size_t i = 0; i < aRows; i++)
    {
        for (size_t j = 0; j < bCols; j++)
        {
            prod->set(i, j, output->get(i,j));
        }
    }

    return prod;
}

binaryOp optimalMultAlgorithm(Matrix const *A, Matrix const *B)
{
    /* heuristic based on online citation strassen = faster if n > 100:
        Skiena, Steven (2008). "Sorting and Searching". The Algorithm
        Design Manual. Springer. pp. 45-46, 401-403.
    */
    if (A->numRows() < 100 && B->numCols() < 100)
    {
        return &naiveMult;
    }
    else
    {
        return &strassenMult;
    }
}
