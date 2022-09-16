# average.py
# Mr. P. Guse
# Key Concepts
#
# variable assignment
# multiplication-division-addition
# integer division - modulus
# round() function
# formatted output (floating-point values) - f-strings in Python

# If you run 10 kilometers in 33 minutes and 14 seconds.
#
# a. What is your average time per mile in minutes and seconds?

miles = 10 * (1 / 1.61)         # number of miles run
seconds = 33*60 + 14            # total time in seconds
time_per_mile = seconds / miles # time per mile in seconds

# Separate the time per mile into minutes and seconds
time_per_mile_minutes = time_per_mile // 60
time_per_mile_seconds = round(time_per_mile % 60)

# Output
print(f"The time per mile was {time_per_mile_minutes} minutes and {time_per_mile_seconds} seconds.")


# b. What is your average speed in miles per hour?

# Since there are 60 seconds in a minute
# and 60 minutes in an hour

hours = seconds * (1/60) * (1/60)  # or ... hours = seconds/60/60
miles_per_hour = miles/hours

# Output
print(f"Your average speed is {miles_per_hour:0.1f} miles per hour.")