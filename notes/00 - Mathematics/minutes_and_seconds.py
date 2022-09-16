# minutes_and_seconds.py
# Mr. P. Guse
# Key concepts
# 
# variable assignment
# integer division - modulus
# formatted output - f-strings in Python

# How many minutes and seconds are there in 1423 seconds?

# Since there are 60 seconds in a minute
minutes = 1423 // 60
# The number of seconds remaining is the
# remainder of 1423 / 60.  This is what the
# modulus operator is used for.
seconds = 1423 % 60

# Output
print(f"In 1423 seconds there are {minutes} minutes and {seconds} seconds.")