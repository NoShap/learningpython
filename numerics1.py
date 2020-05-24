import random
import math


# ----- Python Precendence -----
x = 1
y = 1
# --- Boolean Algebra
x or y				# Logical OR (y is evaluated only if x is false)
x and y 			# Logical AND (y is evaluated only if x is true) 
not x 				# Logical negation
# --- Relational Statements
x in y, x not in y	# Membership (iterables, sets)
x is y, x is not y	# Object identity tests
x < y, x <= y, x > y, x >= y # Magnitude comparison, set subset and superset
x == y, x != y 		# Value equality operators
# --- Binary operators
x | y				# Bitwise OR, set union
x ^ y				# Bitwise XOR, set symmetric difference
x & y				# Bitwise AND, set intersection
x << y, x >> y 		# Shift x left or right by y bits
# --- Arithmetic I
x + y				# Addition, concatenation
x - y				# Subtraction, set difference
# --- Arithmetic II
x * y				# Multiplication, repetition
x % y				# Remainder, format
x / y, x // y		# Division: true and floor
# --- Identity
-x, +x 				# Negation, identity
~x					# Bitwise NOT (inversion)
# --- Exponents
x ** y 				# Power (exponentiation)
# --- Accessing
x[i] 			    # Indexing (sequence, mapping, others)
x[i:j:k]			# Slicing
x(...)				# Call (function, method, class, other callable)
x.attr				# Attribute reference

#Example:
8 * 9 + 3 * 5		# will evaluate multiplications first and then addition



#Type conversion
40 + 3.14       # Integer to float, float math/result
# 43.14

# Variable declaration and assignment 
a = 3                  # Name created: not declared ahead of time
b = 4

a + 1, a - 1           # Addition (3 + 1), subtraction (3 − 1)
#(4, 2)
b * 3, b / 2           # Multiplication (4 * 3), division (4 / 2, 3.X result)
#(12, 2.0)                  
a % 2, b ** 2          # Modulus (remainder), power (4 ** 2)
#(1, 16)
2 + 4.0, 2.0 ** b      # Mixed-type conversions
#(6.0, 16.0)


#Chaining operators
X = 2
Y = 4
Z = 6

X < Y < Z              # Chained comparisons: range tests
# True
X < Y and Y < Z
# True

1 == 2 < 3        # Same as: 1 == 2 and 2 < 3
# False                 # Not same as: False < 3 (which means 0 < 3, which is true!)


#Python 3.X integers support unlimited size:
999999999999999999999999999999 + 1         # 3.X
# 1000000000000000000000000000000

