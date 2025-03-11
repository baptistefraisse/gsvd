""" Example and verification """

# Librairies

import os
import sys
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from gsvd import gsvd

# Example

a = np.array([[1, 6, 11], [2, 7, 12], [3, 8, 13], [4, 9, 14], [5, 10, 15]])
b = np.array([[8, 1, 6], [3, 5, 7], [4, 9, 2]])

gsvd_result = gsvd(a, b)

u_1 = gsvd_result["U1"]
u_2 = gsvd_result["U2"]
s_1 = gsvd_result["S1"]
s_2 = gsvd_result["S2"]
x = gsvd_result["X"]
gamma = gsvd_result["gamma"]

# Printing results

print("U1=", u_1)
print("U2=", u_2)
print("S1=", s_1)
print("S2=", s_2)
print("X=", x)
print("gamma=", gamma)
