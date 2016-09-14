# -*- coding: utf-8 -*-

import numpy as np
from numpy import matrix
from numpy import linalg

#1
A = matrix([[1, 2, 3],[2, 7, 4]])
A.shape

B = matrix([[1, -1],[0, 1]])
B.shape

C = matrix([[5, -1], [9, 1], [6, 0]])
C.shape

D = matrix([[3, -2, -1], [1, 2, 3]])
D.shape

u = matrix([6, 2, -3, 5])
u.shape

v = matrix([3, 5, -1, 4])
v.shape

w = matrix([[1], [8], [0], [5]])
w.shape

#2
np.add(u, v)

np.subtract(u, v)

np.multiply(6, u)

np.dot(u, v) #Doesn't work due to the dimensions
np.dot(u, w) #works because of the dimensions

np.linalg.norm(u) 

#3
np.add(A, C) #not defined

np.subtract(A, C.getT())
"""
Answer
matrix([[-4, -7, -3],
        [ 3,  6,  4]])
"""

C.getT()+np.multiply(3, D)
"""
Answer:
matrix([[14,  3,  3],
        [ 2,  7,  9]])
"""

B * A
"""
Answer
matrix([[-1, -5, -1],
        [ 2,  7,  4]])
"""
np.multiply(B, A.getT()) #not defined


