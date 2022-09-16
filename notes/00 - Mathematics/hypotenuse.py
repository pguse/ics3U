# hypotenuse.py
# Mr. P. Guse
# Key Concepts
#
# variable assignment
# addition-exponentiation
# using the math module - sqrt() function
# formatted output - new-line character \n - f-strings in Python.

# Given a right-angled triangle with side lengths a=5 and b=9, calculuate the hypotenuse c.

import math

a = 5
b = 9
c = math.sqrt(a**2 + b**2)

# Output
print(f"Given a right-angled triangle with side lengths\na = {a} and b = {b}, the hypotenuse is {c:0.1f}.")