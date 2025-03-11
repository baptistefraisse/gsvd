""" Unitary tests """

# Librairies

import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from gsvd import gsvd
import numpy as np


# Class for tests


class TestGSVD(unittest.TestCase):
    """Class for unitary tests"""

    def test_square_matrix(self):
        """Test : 1000 random square matrix with matching sizes from 2 to 100"""

        for _ in range(1000):

            n = np.random.randint(2, 100)
            a = np.random.rand(n, n)
            b = np.random.rand(n, n)

            result = gsvd(a, b)

            u_1 = result["U1"]
            u_2 = result["U2"]
            s_1 = result["S1"]
            s_2 = result["S2"]
            x = result["X"]

            self.assertEqual(
                np.matmul(u_1, np.matmul(s_1, np.transpose(x))).all(), a.all()
            )
            self.assertEqual(
                np.matmul(u_2, np.matmul(s_2, np.transpose(x))).all(), b.all()
            )
            self.assertEqual(
                np.round(np.matmul(u_1, np.transpose(u_1))).all(),
                np.identity(a.shape[0]).all(),
            )
            self.assertEqual(
                np.round(np.matmul(u_2, np.transpose(u_2))).all(),
                np.identity(b.shape[0]).all(),
            )

    def test_rectangular_matrix(self):
        """Test : 1000 random rectangular matrix with matching sizes from 2 to 100"""

        for _ in range(1000):

            c = np.random.randint(2, 100)  # number of columns
            n = np.random.randint(c, 100)  # number of rows for a
            k = np.random.randint(c, 100)  # number of rows for b

            a = np.random.rand(n, c)
            b = np.random.rand(k, c)

            result = gsvd(a, b)

            u_1 = result["U1"]
            u_2 = result["U2"]
            s_1 = result["S1"]
            s_2 = result["S2"]
            x = result["X"]

            self.assertEqual(
                np.matmul(u_1, np.matmul(s_1, np.transpose(x))).all(), a.all()
            )
            self.assertEqual(
                np.matmul(u_2, np.matmul(s_2, np.transpose(x))).all(), b.all()
            )
            self.assertEqual(
                np.round(np.matmul(u_1, np.transpose(u_1))).all(),
                np.identity(a.shape[0]).all(),
            )
            self.assertEqual(
                np.round(np.matmul(u_2, np.transpose(u_2))).all(),
                np.identity(b.shape[0]).all(),
            )

    def test_error_no_facto(self):
        """Test invalid input : A and B are not simultaneously factorizable"""

        a = np.array([[0, 0], [0, 0]])
        b = np.array([[0, 0], [0, 0]])

        with self.assertRaises(ValueError):
            result = gsvd(a, b)

        with self.assertRaises(ValueError):
            result = gsvd(b, a)

    def test_error_size_matching(self):
        """Test invalid input : A and B have unmatching sizes for GSVD"""

        a = np.array([[1, 2, 3], [4, 5, 6]])
        b = np.array([[7, 8], [9, 10]])

        with self.assertRaises(ValueError):
            result = gsvd(a, b)

        with self.assertRaises(ValueError):
            result = gsvd(b, a)

    def test_error_void(self):
        """Test invalid input : A and B are void"""

        a = np.array([])
        b = np.array([])

        with self.assertRaises(ValueError):
            result = gsvd(a, b)

        with self.assertRaises(ValueError):
            result = gsvd(b, a)

    def test_error_too_small(self):
        """Test invalid input : A and B are too small"""

        a = np.array([1])
        b = np.array([2])

        with self.assertRaises(ValueError):
            result = gsvd(a, b)

        with self.assertRaises(ValueError):
            result = gsvd(b, a)


# Run tests

if __name__ == "__main__":
    unittest.main()
