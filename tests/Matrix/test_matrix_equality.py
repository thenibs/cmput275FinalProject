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
from copy import deepcopy

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


class TestMatrixEquality(unittest.TestCase):
    def test_equal_from_same_vals_list_3x3(self):
        A1 = Matrix(a_vals)
        A2 = Matrix(a_vals)

        self.assertEqual(A1, A2,
                         'Matrices initialized with same values list \
                                                            are not equal')

    def test_equal_from_equivalent_vals_list_3x3(self):
        a_vals_copy = deepcopy(a_vals)
        A1 = Matrix(a_vals)
        A2 = Matrix(a_vals_copy)

        self.assertEqual(A1, A2,
                         'Matrices inititialized with the same values \
                                        from different lists are not equal')

    def test_not_equal_with_different_vals_list_3x3(self):
        A = Matrix(a_vals)
        B = Matrix(b_vals)

        self.assertNotEqual(A, B)

    def test_not_equal_with_almost_same_vals_list_3x3(self):
        almost_a_vals = deepcopy(a_vals)
        a_vals[0][1] += 1

        A = Matrix(a_vals)
        almost_A = Matrix(almost_a_vals)

        self.assertNotEqual(A, almost_A)

    def test_equal_to_numpy_mat_with_same_vals_list_3x3(self):
        A = Matrix(a_vals)
        np_A = np.array(a_vals)

        self.assertEqual(A, np_A)

    def test_not_equal_to_numpy_mat_with_different_vals_3x3(self):
        A = Matrix(a_vals)
        np_B = np.array(b_vals)

        self.assertNotEqual(A, np_B)

    def test_equal_to_numpy_mat_with_same_vals_2x3(self):
        C = Matrix(c_vals)
        np_C = np.array(c_vals)

        self.assertEqual(C, np_C)
