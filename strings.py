# Author: Noah Shapiro All Rights Reserved, copyright 2020 © 
# Date: 5/24/2020
# Project: Learning Python
# Module: strings.py
import re
import sys

# Intro: There are three major types of basic objects within Python
# NUMBERS(Integer, floating-point, decimal, fraction)
# -- support addition, multiplication...
# SEQUENCES(strings, lists, tuples)
# -- supports indexing, slicing, concatenation...
# MAPPINGS(dictionaries)
# -- supports indexing by keys


# Also remember the immutable types and mutable types overlap
# these three categories:
# IMMUTABLES(numbers, strings, tuples, frozensets)
# -- None of these objects can be changed, need to use methods or other
# expressions which will create copies that can be assigned to other vars
# MUTABLES(lists, dictionaries, sets, bytearrays)
# -- Conversely, these objects can always be changed in place. Useful,
# but be careful when you change one mutable object, you are not changing 
# multiple references to that object unintentionally


S = '' 						# Empty string
S = "spam's"			  	# Double quotes, same as single
S = 's\np\ta\x00m' 		  	# Escape sequences
S = """...multiline...
""" 						# Triple-quoted block strings
print(S)
S = r'\temp\spam'			# Raw strings (no escapes)
B = b'sp\xc4m'				# Byte strings in 2.6, 2.7, and 3.X 

i = 0
j = 2

S[i]						# Index
S[i:j]						# Slice 
len(S)						# Length

S = "a %s parrot" % 'kind'	# String formatting expression

# Useful String functions
S.find('pa')				# String methods (see ahead for all 43): search,
S.rstrip()					# remove whitespace
S.replace('pa', 'xx')		# replacement
S.split(',')				# split on delimiter
S.isdigit()					# content test
S.lower()					# case conversion
S.endswith('spam')			# end test
'spam'.join(' ')			# delimiter join
S.encode('latin-1')			# Unicode encoding 

# All different escape characters:
'\\ \' \" \a \b \f \n \r \t \v'


'abc' + 'def'         # Concatenation: a new string
# 'abcdef'
'Ni!' * 4             # Repetition: like "Ni!" + "Ni!" + ...
# 'Ni!Ni!Ni!Ni!'

# multiplication useful for printing multiple lines Example:
print('-' * 80)     

# you can use negative offsets unlike in C
S = 'spam'
S[0], S[-2]                         # Indexing from front or end
('s', 'a')
S[1:3], S[1:], S[:-1]               # Slicing: extract a section
('pa', 'pam', 'spa')

"hello"[::-1] 						# Reverse a string with smart slicing


# ----- Changing Strings -----
# Create new strings
S = 'spam'
# S[0] = 'x'                 # Raises an error!

S = S + 'SPAM!'            # To change a string, make a new one
'spamSPAM!'

S = S[:4] + 'Burger' + S[-1]
'spamBurger!'

# Replace function
S = 'splot'
S = S.replace('pl', 'pamal')
S
'spamalot'



# ----- Useful Methods ----- 
# --- .replace()
S = 'spammy'
S = S.replace('mm', 'xx')         # Replace all mm with xx in S
'spaxxy'

# sometimes however in order to change a string you'll want 
# to convert it into a mutable List objects
S = 'spammy'
L = list(S)
['s', 'p', 'a', 'm', 'm', 'y']

L[3] = 'x'                        # Works for lists, not strings
L[4] = 'x'
['s', 'p', 'a', 'x', 'x', 'y']

# convert back as such:
S = ''.join(L)
'spaxxy'

# --- .split()
line = 'bob,hacker,40'
line.split(',')
['bob', 'hacker', '40']


# More on Formatting strings

'That is %d %s bird!' % (1, 'dead') 

#using variables

exclamation = 'Ni'
'The knights who say %s!' % exclamation  

'%s -- %s -- %s' % (42, 3.14159, [1, 2, 3])     # All types match a %s target
'42 -- 3.14159 -- [1, 2, 3]'

"""
# formatiting type codes:
s 			# String (or any object’s str(X) string)
r 			# Same as s, but uses repr, not str
c 			# Character (int or str)
d 			# Decimal (base-10 integer)
i 			# Integer
u 			# Same as d (obsolete: no longer unsigned)
o 			# Octal integer (base 8)
x 			# Hex integer (base 16)
X 			# Same as x, but with uppercase letters
e 			# Floating point with exponent, lowercase
E 			# Same as e, but uses uppercase letters
f 			# Floating-point decimal
F  			# Same as f, but uses uppercase letters
g 			# Floating-point e or f
G 			# Floating-point E or F
# % 			# Literal % (coded as %%)
"""

#Can also use dictionaries for formatting strings (pretty cool)
'%(qty)d more %(food)s' % {'qty': 1, 'food': 'spam'}
'1 more spam'

#effective uses
reply = """
Greetings...
Hello %(name)s!
Your age is %(age)s
"""
values = {'name': 'Bob', 'age': 40}       # Build up values to substitute
print(reply % values)                     # Perform substitutions












