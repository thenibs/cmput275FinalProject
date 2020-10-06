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
    [0, 3, 1],
]

c_vals = [
    [1, -4],
    [3, 4],
    [0, 1]
]

class TestMatrixScale(unittest.TestCase):
    def test_scaling_3x3(self):
        A = Matrix(a_vals)
        np_A = np.array(a_vals)

        self.assertEqual(3 * A, 3 * np_A)

    def test_scaling_2x3(self):
        B = Matrix(b_vals)
        np_B = np.array(b_vals)

        self.assertEqual(2 * B, 2 * np_B)

    def test_scaling_3x2(self):
        C = Matrix(c_vals)
        np_C = np.array(c_vals)

        self.assertEqual(-1 * C, -1 * np_C)

    def test_scaling_by_1_leaves_unchanged(self):
        D = Matrix.fill(3, 4, 2)
        self.assertEqual(D, 1 * D)