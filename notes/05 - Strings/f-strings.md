# Python f-Strings

Python **f-strings** or **formatted string literals** contain expressions in curly braces which are evaluated at run-time.  For example,

```python
name = "Mr. Guse"
age = 51

fstring = f"{name} is {age} years old."

print(fstring)
```

produces the output

```
Mr. Guse is 51 years old.
```

An advantage of Python f-strings is the ability to execute expressions at runtime. This means that you aren’t restricted to only inserting variable names. For example,

```python
fstring = f"1 + 1 = {1+1}."
print(fstring)
```

produces the output

```
1 + 1 = 2
```

## Formatted Output with f-strings

You can use a number of different symbols to align text with f-strings. For example, you can use any of <, >, ^ _(for left, right, and centered alignment, respectively)_, followed by a digit of values of space reserved for the string. For example,

```python
course = "Mathematics"
mark = 87.563
print(f"{course:^15} {mark:>10}")
print(f"{course:<15} {mark:>10}")
print(f"{course:>15} {mark:>10}")
```

creates a **column width** of 15 characters for the course name and 10 characters for the mark, and produces the output

```
  Mathematics       87.563
Mathematics         87.563
    Mathematics     87.563
```

You can control the number of decimals places displaying for a **floating-point** value.  For example, if you want only 1 decimal place displayed,

```python
print(f"{course:>15} {mark:>10.1f}")
```

produces the output

```
    Mathematics       87.6
```

If you don't want to create a column of space for your values, you can just do the following,

```python
print(f"Mark: {mark:0.2f}")
```

with an output of

```
Mark: 87.56
```

You can also automatically format **floating-point** values in different styles.  For example, if you have a value that represents a percentage as a decimal, you can output the value as a **percent**.

```python
average = 0.76548
print(f"Average: {average:0.2%}")
```

produces the output

```
Average: 76.55%
```

You can also automatically display values use **exponential _(scientific)_ notation**.

```python
density = 0.0025461
print(f"Density: {density:0.3e}")
```

produces the output

```
Density: 2.546e-03
```