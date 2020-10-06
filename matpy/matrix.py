# ---------------------------------------------------
# Name: Ahmad Amin, Yash Bhandari & Nibras Alam
# ID: 1623338, 1616539 & 1617818
# CMPUT 275, Winter 2020
#
# Final Project
#
# Consulted Python Documentation
# ---------------------------------------------------
from . import _Matrix  # c++ Matrix implementation
import numpy as np

# function decorator to wrap c++ matrices in a python Matrix
def wrap_cpp_matrix(func):
    def wrapped(*args, **kwargs):
        return Matrix(cpp_matrix=func(*args, **kwargs))

    return wrapped


class Matrix:
    def __init__(self, matrix_values=[[0]], cpp_matrix=None):
        """
        Args:
            matrix_values: 2D list or Matrix from which to initialize values
        """
        if cpp_matrix:
            self._mat = cpp_matrix
        else:
            self._mat = _Matrix(matrix_values)

    def __getitem__(self, indices):
        """
        Args:
            indices: a tuple (i, j) representing indices of a matrix entry
        Returns:
            the i,j-th entry of the matrix
        """
        return self._mat.get(indices[0], indices[1])

    @wrap_cpp_matrix
    def __add__(self, other: 'Matrix') -> 'Matrix':
        """
        Args:
            other: another matrix of the same dimensions
        Returns:
            The matrix sum of self and other
        """
        return self._mat.add(other._mat)

    @wrap_cpp_matrix
    def __matmul__(self, other: 'Matrix') -> 'Matrix':
        """
        Distinct from __mul__ to comply with PEP 465
        Args:
            other: another matrix of the same dimensions
        Returns:
            The matrix product of self and other
        """
        return self._mat.mult(other._mat)

    @wrap_cpp_matrix
    def __mul__(self, scalar: int) -> 'Matrix':
        """
        Args:
            scalar: an integer
        Returns:
            The matrix scalar product
        """
        return self._mat.scale(scalar)

    @wrap_cpp_matrix
    def __rmul__(self, scalar: int) -> 'Matrix':
        """
        Args:
            scalar: an integer
        Returns:
            The matrix scalar product
        """
        return self._mat.scale(scalar)

    @wrap_cpp_matrix
    def __pow__(self, pow: int) -> 'Matrix':
        """
        Args:
            pow: a non negative integer
        Returns:
            This matrix raised to the given power
        """
        return self._mat.exp(pow)

    def __eq__(self, other):
        """
        Args:
            other: Another matrix or numpy array
        Returns:
            True if the two matrices are equal
        """
        if isinstance(other, np.ndarray):
            return self.__equals_numpy_array(other)
        if not isinstance(other, Matrix):
            return False
        return self._mat.equals(other._mat)

    def __equals_numpy_array(self, np_array):
        """
        Compares with numpy array
        """
        if self.dim != np_array.shape:
            return False

        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                if self[i,j] != np_array[i,j]:
                    return False
        return True
    
    def __str__(self):
        return self._mat.str()

    def __repr__(self):
        return self.__str__()

    @property
    def dim(self):
        """
        Returns the dimension of the matrix as a tuple
        """
        return self._mat.dim()

    @classmethod
    @wrap_cpp_matrix
    def id(cls, n):
        """
        Constructs an n x n identity matrix
        """
        return _Matrix.id(n)

    @classmethod
    @wrap_cpp_matrix
    def fill(cls, m, n, fill=0):
        """
        Constructs an m x n matrix with all entries set to the fill parameter
        """
        return _Matrix(m, n, fill)

    @classmethod
    @wrap_cpp_matrix
    def naive_mult(cls, A, B):
        """
        Uses a naive matrix multiplication algorithm to compute A*B
        """
        return _Matrix.naive_mult(A._mat, B._mat)

    @classmethod
    @wrap_cpp_matrix
    def strassen_mult(cls, A, B):
        """
        Uses the strassen algorithm to compute the product of A and B
        """
        return _Matrix.strassen_mult(A._mat, B._mat)
