# ---------------------------------------------------
# Name: Ahmad Amin, Yash Bhandari & Nibras Alam
# ID: 1623338, 1616539 & 1617818
# CMPUT 275, Winter 2020
#
# Final Project
#
# Consulted Python Documentation
# ---------------------------------------------------

# This file shows how our matpy library can be used
# Begin by importing the Matrix class from matpy
from matpy import Matrix

# matpy matrices can be constructed from a 2d python list of integers
A = Matrix([
    [1, 2, 3],
    [4, 5, 6]
])
# They have a pretty representation when printed
print('A =', A)

# Matrices can also be contructed from factory methods
# This creates a 3 x 2 matrix with all entries set to 3
all_threes = Matrix.fill(3, 2, 3)
print('all_threes =', all_threes)

# This creates a 3 x 3 identity matrix
id_3 = Matrix.id(3)
print('id_3 =', id_3)

# You can find a Matrix's dimension with .dim
print('A.dim =', A.dim)

# You can access a particular entry
print('A[0, 1] =', A[0,1])
# However, matrices are immutable so you cannot set a particular entry

# Matrices can also be added
B = id_3 + Matrix.fill(3, 3, 1)
print('B =', B)

# Matrices can be scaled by other integers with the * operator
print('0A =', 0*A)

# And they can be multiplied using the @ operator
print('AB =', A @ B)

# While the multiplication algorithm is decided heuristically for each pair of matrices,
# you can also explicitly use a particular algorithm
Matrix.naive_mult(A, B)
Matrix.strassen_mult(A, B) 

# You can also raise matrices to nonnegative integer powers
D = Matrix([
    [1, 1],
    [2, -1]
])
print('D^2 =', D**2)

# You can check for equality with the == operator
print('Does A == D?', A == D)

# This even works with numpy matrices (so long as the matpy matrix is on the left)
import numpy as np
np_D = np.array([
    [1, 1],
    [2, -1]
])
print ('Does D == np_D?', D == np_D)