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
    [1, 0, 0],
    [1, 2, 0],
    [0, 0, 2]
]

class TestMatrixExponentiation(unittest.TestCase):
    def test_raising_3x3_to_2(self):
        A = Matrix(a_vals)
        np_A = np.array(a_vals)

        self.assertEqual(A ** 2, np.linalg.matrix_power(np_A, 2))

    def test_raising_3x3_to_3(self):
        A = Matrix(a_vals)
        np_A = np.array(a_vals)

        self.assertEqual(A ** 3, np.linalg.matrix_power(np_A, 3))

    def test_raising_id_leaves_unchanged(self):
        id_4 = Matrix.id(4)

        self.assertEqual(id_4, id_4 ** 6)

    def test_raises_exception_for_non_square_matrix(self):
        B = Matrix.fill(3, 2, 0)

        with self.assertRaises(Exception):
            B ** 3