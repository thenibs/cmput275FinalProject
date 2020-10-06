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
from matpy import Matrix

a_vals = [
    [1, 2, 3],
    [4, 5, 6],
]

id3_vals = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]


class TestMatrixInstantiation(unittest.TestCase):
    def test_matrix_from_vals_has_correct_dim(self):
        A = Matrix(a_vals)
        correct_dim = (len(a_vals), len(a_vals[0]))
        self.assertEqual(A.dim, correct_dim)

    def test_matrix_from_vals_has_same_entries(self):
        A = Matrix(a_vals)
        for i in range(len(a_vals)):
            for j in range(len(a_vals)):
                self.assertEqual(a_vals[i][j], A[i, j])

    def test_id_matrix_creates_id(self):
        test_id3 = Matrix.id(3)
        real_id3 = Matrix(id3_vals)

        self.assertEqual(test_id3, real_id3)

    def test_matrix_fill_is_of_correct_dim(self):
        A = Matrix.fill(3, 4)
        self.assertEqual(A.dim, (3, 4))

    def test_matrix_fill_has_all_elements_set_correctly(self):
        all_5 = Matrix.fill(6, 3, 5)
        for i in range(all_5.dim[0]):
            for j in range(all_5.dim[1]):
                self.assertEqual(all_5[i,j], 5)

