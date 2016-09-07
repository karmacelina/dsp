# Matrix Algebra

import sympy
from sympy.interactive.printing import init_printing
init_printing(use_unicode = False, wrap_line = False, no_global = True)
from sympy.matrices import *

A = Matrix([[1, 2, 3], [2, 7, 4]])
B = Matrix([[1, -1], [0, 1]])
C = Matrix([[5, -1], [9, 1], [6,0]])
D = Matrix([[3, -2, -1], [1, 2, 3]])

u = Matrix([[6, 2, -3, 5]])
v = Matrix([[3, 5, -1, 4]])
w = Matrix([1, 8, 0, 5])

# 1 Matrix dimensions:
print "Exercise 1: Matrix dimensions\n"

# 1.1
print "1.1: The shape of matrix A is", A.shape

#1.2
print "1.2: The shape of matrix B is", B.shape

#1.3
print "1.3: The shape of matrix C is", C.shape

#1.4
print "1.4: The shape of matrix D is", D.shape

#1.5
print "1.5: The shape of matrix u is", u.shape

#1.6
print "1.6: The shape of matrix w is", w.shape

# 2 Vector operations:
print "\nExercise 2: Vector operations\n"

# 2.1
print "2.1: The sum of u and v is", u + v

#2.2
print "2.2: The difference between u and v is", u - v

#2.3
alpha = 6
print "2.3: The product of alpha and u is:", alpha*u

#2.4
print "2.4: The dot product between u and v is", u.dot(v)

#2.5
print "2.5: The magnitude of u is", u.dot(u)**0.5 #Should I have formatted this float?

# 3 Matrix Operations:
print "\n Exercise 3: Matrix operations\n"

#3.1
print "3.1: The sum of A and C is not defined."

#3.2
print "3.2: A - transpose(C) =", A - C.T

#3.3
print "3.3: transpose(C) + 3*D =", C.T + 3*D

#3.4
print "3.4: BA =", B*A

#3.5
print "3.5: B*transpose(A) is not defined."

#3.6
print "3.6: B*C is not defined."

#3.7
print "3.7: C*B =", C*B

#3.8
print "3.8: B^4 =", B**4

#3.9
print "3.9: A*transpose(A) =", A*A.T

#3.10
print "3.10: transpose(D)* D =", (D.T)*D