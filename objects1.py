# Author: Noah Shapiro All Rights Reserved, copyright 2020 © 
# Date: 5/23/2020
# Project: Learning Python
# Module: objects1.py


import math
import random
import re # Regular Expression pattern matching module

random.random()
# 0.7082048489415967
random.choice([1, 2, 3, 4])
# 1

# ----- Math/Numerics -----
print(math.pi)

math.sqrt(85)

123 + 222                    # Integer addition

1.5 * 4                      # Floating-point multiplication

2 ** 100                     # 2 to the power 100, again

# ----- Strings -----
S = 'Spam'

len(S)               # Length
4
S[0]                 # The first item in S, indexing by zero-based position
# 'S'
S[1]                 # The second item from the left
# 'p'

S[-1]				 # Count backwards
# m

S[1:3]                # Slice of S from offsets 1 through 2 (not 3)
# 'pa'

S[1:]                 # Everything past the first (1:len(S))

S[:3]                 # Same as S[0:3]
# 'Spa'

S[:-1]                # Everything but the last again, but simpler (0:-1)
# 'Spa'

S[:]	# All of S as a top-level copy (0:len(S))


# Immutability Exmple
# numbers, strings, and tuples are immutable ...

S + 'xyz'             # Concatenation (but not changing the string)



# ... lists, dictionaries, and sets are not
S = 'shrubbery'
L = list(S)                                     # Expand to a list: [...]
L
['s', 'h', 'r', 'u', 'b', 'b', 'e', 'r', 'y']
L[1] = 'c'                                      # Change it in place
''.join(L)                                      # Join with empty delimiter
# 'scrubbery'


line = 'aaa,bbb,ccccc,dd'
line.split(',')              # Split on a delimiter into a list of substrings
# ['aaa', 'bbb', 'ccccc', 'dd']

S = 'spam'
S.upper()                    # Upper- and lowercase conversions
# 'SPAM'
S.isalpha()                  # Content tests: isalpha, isdigit, etc.
# True

line = 'aaa,bbb,ccccc,dd\n'
line.rstrip()                # Remove whitespace characters on the right side
# 'aaa,bbb,ccccc,dd'
line.rstrip().split(',')     # Combine two operations
# ['aaa', 'bbb', 'ccccc', 'dd']

'%s, eggs, and %s' % ('spam', 'SPAM!')          # Formatting expression (all)
# 'spam, eggs, and SPAM!'

# Returns list of all attributes in an object including implementation details '__X__' and methods
dir(S)
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', 
# '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', 
# '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', 
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__',
# '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 
# 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 
# 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 
# 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 
# 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 
# 'title', 'translate', 'upper', 'zfill']

# Can then use help function to find out more about a method
# help(S.replace)

# Escape Characters
S = 'A\nB\tC'            # \n is end-of-line, \t is tab

# gives ordinance of a specific char (ASCII value)
ord('\n') 


# ----- Lists -----

L = [123, 'spam', 1.23]

# Can index, slice and concatenate just like Strings / other sequences
L[0]                               # Indexing by position
123
L[:-1]                             # Slicing a list returns a new list
[123, 'spam']

L + [4, 5, 6]                      # Concat/repeat make new lists too
[123, 'spam', 1.23, 4, 5, 6]
L * 2
# [123, 'spam', 1.23, 123, 'spam', 1.23]

L                                  # We're not changing the original list
# [123, 'spam', 1.23]

# Methods
L.append('NI')                     # Growing: add object at end of list
# [123, 'spam', 1.23, 'NI']
L.pop(2)                           # Shrinking: delete an item in the middle

# Because lists are mutable, most list methods also change the list object in place, instead of creating a new one:
M = ['bb', 'aa', 'cc']
M.sort()
# ['aa', 'bb', 'cc']

M.reverse()
# ['cc', 'bb', 'aa']

N = [[1, 2, 3],               # A 3 × 3 matrix, as nested lists
    [4, 5, 6],               # Code can span lines if bracketed
    [7, 8, 9]]

N[1]                          # Get row 2
# [4, 5, 6]

N[1][2]                       # Get row 2, then get item 3 within the row
# 6

#List comprehensions
col2 = [r[1] for r in N]             # Collect the items in column 2
#[2, 5, 8]

#more complex List comprehensions
[row[1] + 1 for row in N]                 # Add 1 to each item in column 2
# [3, 6, 9]

[row[1] for row in N if row[1] % 2 == 0]  # Filter out odd items
# [2, 8]

diag = [N[i][i] for i in [0, 1, 2]]      # Collect a diagonal from matrix
# [1, 5, 9]


# ----- Dictionaries -----
D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}

D['food']              # Fetch value of key 'food'
# 'Spam'

D['quantity'] += 1     # Add 1 to 'quantity' value
print(D)
# {'color': 'pink', 'food': 'Spam', 'quantity': 5}


'f' in D 			   # in membership expression allows us to know if a dict contains a certain key
# False

# if not 'f' in D 	   # combining conditionals with boolean expressions
	# Do something 


# ----- Tuples -----
# Very similar to lists except they are immutable so they provide some sort of
# certainty that they will not be changed by random methods like .append()

T = (1, 2, 3, 4)            # A 4-item tuple
len(T)                      # Length
4

T + (5, 6)                   # Concatenation
# (1, 2, 3, 4, 5, 6)

T[0]                        # Indexing, slicing, and more
# 1

# T[0] = 2                    # Tuples are immutable so this line will not work!
# ...error text omitted...
# TypeError: 'tuple' object does not support item assignment

T = (2,) + T[1:]            # Make a new tuple for a new value
# (2, 2, 3, 4)


# ----- Tuples -----
# File objects are Python codes object to interact with files on your computer!

f = open('data.txt', 'w')      # Make a new file in output mode ('w' is write)
f.write('Hello\n')             # Write strings of characters to it
6
f.write('world\n')             # Return number of items written in Python 3.X
6
f.close()                      # Close to flush output buffers to disk



