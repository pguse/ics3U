## Answers

1. How many seconds are there in 13 minutes and 13 seconds?

```python
# Since there are 60 seconds in a minute
seconds = 13*60 + 13

# Output
print(f"There are {seconds} seconds in 13 minutes and 13 seconds.")
```

### Output
```There are 793 seconds in 13 minutes and 13 seconds.```


2. How many miles are in 10 kilometers? _(1 mile is 1.61 kilometers)_

```python
miles = 10 *(1 / 1.61)

# Output
print(f"There are {miles:0.2f} miles in 10 kilometers.")
```

### Output
```There are 6.21 miles in 10 kilometers.```


3. How many minutes and seconds are there in 1423 seconds?

```python
# Since there are 60 seconds in a minute
minutes = 1423 // 60
# The number of seconds remaining is the
# remainder of 1423 / 60.  This is what the
# modulus operator is used for.
seconds = 1423 % 60

# Output
print(f"In 1423 seconds there are {minutes} minutes and {seconds} seconds.")
```

### Output
```In 1423 seconds there are 23 minutes and 43 seconds.```


4. If you run 10 kilometers in 33 minutes and 14 seconds,

		a. What is your average time per mile in minutes and seconds?
		b. What is your average speed in miles per hour?

```python
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
```

### Output
```
The time per mile was 5.0 minutes and 21 seconds.
Your average speed is 11.2 miles per hour.
```


5. The **volume** of a **sphere** with a radius **r** is 
<img src="https://render.githubusercontent.com/render/math?math=\frac{4}{3} \pi r^3">.  What is the **volume** of a **sphere** with a radius of 5 ?

```python
import math

radius = 5
volume = (4/3)*math.pi*radius**3

# Output
print(f"The volume of a sphere of radius {radius} is {volume:0.0f}.")
```


### Output
```The volume of a sphere of radius 5 is 524.```


6.  Given a right angled triangle with side lengths **a = 5** and **b = 9**, calculate the _hypotenuse_ **c**

```python
import math

a = 5
b = 9
c = math.sqrt(a**2 + b**2)

# Output
print(f"Given a right-angled triangle with side lengths\na = {a} and b = {b}, the hypotenuse is {c:0.1f}.")
```

### Output
```
Given a right-angled triangle with side lengths
a = 5 and b = 9, the hypotenuse is 10.3.
```