# volume.py
# Mr. P. Guse
# Key Concepts
#
# variable assignment
# multiplication-division-exponentiation
# using the math module - value of pi
# formatted output - no decimals - f-strings in Python.

# What is the volume of a sphere of radius 5?

import math

radius = 5
volume = (4/3)*math.pi*radius**3

# Output
print(f"The volume of a sphere of radius {radius} is {volume:0.0f}.")