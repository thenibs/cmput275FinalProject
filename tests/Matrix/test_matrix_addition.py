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
    [1, 2, 3],
    [3, 4, 5],
    [6, 7, 8]
]

b_vals = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

c_vals = [
    [1, 3, 5],
    [2, 4, 6]
]

d_vals = [
    [7, 2, 3],
    [1, 3, 6]
]


class TestMatrixAddition(unittest.TestCase):
    def test_adding_to_self_3x3(self):
        A = Matrix(a_vals)
        np_A = np.array(a_vals)

        self.assertEqual(A + A, np_A + np_A)

    def test_adding_to_other_same_dim_3x3(self):
        A = Matrix(a_vals)
        np_A = np.array(a_vals)
        B = Matrix(b_vals)
        np_B = np.array(b_vals)

        self.assertEqual(A + B, np_A + np_B)

    def test_adding_to_other_same_dim_2x3(self):
        C = Matrix(c_vals)
        np_C = np.array(c_vals)
        D = Matrix(d_vals)
        np_D = np.array(d_vals)

        self.assertEqual(C + D, np_C + np_D)

    def test_adding_to_self_2x3(self):
        C = Matrix(c_vals)
        np_C = np.array(c_vals)

        self.assertEqual(C + C, np_C + np_C)

    def test_exception_raised_when_adding_matrices_of_different_dimension(self):
        A = Matrix(a_vals)
        C = Matrix(c_vals)

        with self.assertRaises(Exception):
            A + C

    def test_addition_is_commutative(self):
        C = Matrix(c_vals)
        np_C = np.array(c_vals)
        D = Matrix(d_vals)
        np_D = np.array(d_vals)

        self.assertEqual(C + D, D + C)
