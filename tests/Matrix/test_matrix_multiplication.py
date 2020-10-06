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

a_vals = [
    [1, 7],
    [4, 9]
]

b_vals = [
    [11, 13, 17],
    [19, 23, 29]
]

class TestMatrixMultiplication(unittest.TestCase):
    def test_multiplying_with_id_returns_same_matrix_2x2(self):
        A = Matrix(a_vals)
        id2 = Matrix.id(2)

        self.assertEqual(A @ id2, A)
        self.assertEqual(id2 @ A, A)

    def test_multiplying_2x2_with_2x3(self):
        A = Matrix(a_vals)
        np_A = np.array(a_vals)
        B = Matrix(b_vals)
        np_B = np.array(b_vals)

        self.assertEqual(A @ B, np_A @ np_B)

    def test_throws_error_when_matrices_wrong_dimension_2x2_with_3x3(self):
        A = Matrix(a_vals)
        id3 = Matrix.id(3)

        with self.assertRaises(Exception):
            A @ id3

    def test_throws_error_when_matrices_wrong_dimension_2x3_with_2x2(self):
        A = Matrix(a_vals)
        B = Matrix(b_vals)

        with self.assertRaises(Exception):
            B @ A
