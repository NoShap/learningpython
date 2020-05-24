import random
import math
from decimal import Decimal
from fractions import Fraction



# ----- Python Precendence -----
x = 1
y = 1
# --- Boolean Algebra
x or y				# Logical OR (y is evaluated only if x is false)
x and y 			# Logical AND (y is evaluated only if x is true) 
not x 				# Logical negation
# --- Relational Statements
# x in y, x not in y	# Membership (iterables, sets)
# x is y, x is not y	# Object identity tests
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
# s[i] 			    # Indexing (sequence, mapping, others)
# s[i:j:k]			# Slicing
# s(...)				# Call (function, method, class, other callable)
# s.attr				# Attribute reference

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


# Useful math functions
import math
math.pi, math.e                               # Common constants
#(3.141592653589793, 2.718281828459045)

math.sin(2 * math.pi / 180)                   # Sine, tangent, cosine
#0.03489949670250097

math.sqrt(144), math.sqrt(2)                  # Square root; Math Module imported
#(12.0, 1.4142135623730951)

144 ** .5                   			  	  # Expression

pow(2, 4), 2 ** 4, 2.0 ** 4.0                 # Exponentiation (power); Built-In
#(16, 16, 16.0)

abs(-42.0), sum((1, 2, 3, 4))                 # Absolute value, summation
#(42.0, 10)

min(3, 1, 2, 4), max(3, 1, 2, 4)              # Minimum, maximum
#(1, 4)

#Decimals and Fractions
Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
# Decimal('0.0')



x = Fraction(1, 3)                    # Numerator, denominator
y = Fraction(4, 6)                    # Simplified to 2, 3 by gcd

x
# Fraction(1, 3)
y
# Fraction(2, 3)
print(y)
# 2/3

x + y
# Fraction(1, 1)
x - y                           # Results are exact: numerator, denominator
# Fraction(−1, 3)
print(x * y)
# Fraction(2, 9)

#Fractions can also be created from floating point numbers

Fraction('.25')
# Fraction(1, 4)
Fraction('1.25')
# Fraction(5, 4)
Fraction('.25') + Fraction('1.25')
# Fraction(3, 2)



#Also have Set types 
# Can be useful for removing duplicates and can be moved between list and set type quickly

t = set('abcde')
u = set('bdxyz')

t
# set(['a', 'c', 'b', 'e', 'd'])                   # Pythons <= 2.6 display format

t − u                                        # Difference
# set(['a', 'c', 'e'])

t | u                                        # Union
# set(['a', 'c', 'b', 'e', 'd', 'y', 't', 'z'])

t & u                                        # Intersection
# set(['b', 'd'])

t ^ u                                        # Symmetric difference (XOR)
# set(['a', 'c', 'e', 'y', 't', 'z'])

t > u, t < u                                 # Superset, subset
# (False, False)

#Bool Type

