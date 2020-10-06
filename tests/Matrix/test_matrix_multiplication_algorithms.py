# ---------------------------------------------------
# Name: Ahmad Amin, Yash Bhandari & Nibras Alam
# ID: 1623338, 1616539 & 1617818
# CMPUT 275, Winter 2020
#
# Final Project
#
# Consulted Python Documentation
# ---------------------------------------------------
import unittest
import numpy as np
from matpy import Matrix
from ddt import ddt, data
from .multiply_test_data import naive_pairs, strassen_pairs, matrices

@ddt
class TestMatrixMultiplicationAlgorithms(unittest.TestCase):
    """
    Uses the ddt library to generate test cases for each pair of matrices
    that can be multiplied in multiply_pairs.
    Generates test cases for both the naive_mult and strassen_mult algorithms
    """
    @data(*strassen_pairs)
    def test_strassen_multiplication(self, value):
        a, b = value
        A, np_A = Matrix(matrices[a]), np.array(matrices[a])
        B, np_B = Matrix(matrices[b]), np.array(matrices[b])

        prod = Matrix.strassen_mult(A, B)
        true_prod = np_A @ np_B
        self.assertEqual(prod, true_prod,
            f'\nUsing Strassen to multiply \n{A} \n\nwith \n{B}\n'
            f'\ngave incorrect answer \n{prod} \n\nExpected: \n{true_prod}')

    @data(*naive_pairs)
    def test_naive_multiplication(self, value):
        a, b = value
        A, np_A = Matrix(matrices[a]), np.array(matrices[a])
        B, np_B = Matrix(matrices[b]), np.array(matrices[b])

        prod = Matrix.naive_mult(A, B)
        true_prod = np_A @ np_B
        self.assertEqual(prod, true_prod,
            f'\nUsing Strassen to multiply \n{A} \n\nwith \n{B}\n'
            f'\ngave incorrect answer \n{prod} \n\nExpected: \n{true_prod}')