# Making Decisions

All programs have been executed sequentially, line by line, up to this point.  Often programs need to make decisions based on certain conditions determined by the value of a variable.  In Python, decisions are made using the if / elif /else statement.

## Comparison Operators

These statements require that you use one of a number of comparison operators.  For example,

* \<   ***(less than)*** the condition is true if left side is less than right side. 
* \>   ***(greater than)*** the condition is true if left side is greater than right side. 
* \<\=  ***(less than or equal)***
* \>\=  ***(greater than or equal)***
* \=\=  ***(equal to)***
* \!\=  ***(not equal to)***

Here are some examples using and **if/else** statement in Python:

```python
n = int(input("Enter a number: "))

if n % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
```

If there are more than two options, then the **if/elif/else** could be used,

```python
mark = int(input("Enter your current mark: "))

if mark >= 80:
    print("A")
elif mark >= 70:
    print("B")
elif mark >= 60:
    print("C")
elif mark >= 50:
    print("D")
else:
    print("You are not meeting course expectations.")
```

In both examples above, only one of the available options will be acted upon in an **if/elif/else** block of code.  You can have as many **elif's** as you need ***(including none)*** .  You should at least have an **if** and **else** if there are only two options, but even the **else** can be omitted.

## Boolean Values & Logical Operators

All **if/elif/else** statements use **Boolean** values, even though that may not be apparent.  For example,

* print( 3 > 1) produces the value **True**
* print( 2 < 5 ) produces the value **False**.

For example, the code

```python
print(3 > 1)
print(2 < 5)
```

produces

```
True
False
```

The values **True** and **False** are called **Boolean** values.

If you need to test more than one condition you may need to use a **logical operator**.  In Python, the logical operators are the keywords **and** and **or**.  For example,

* print( 3 > 1 **or** 2 < 5) produces the value **True** because one of the conditions is true.  Both conditions must be false to produce the value **False**.
* print( 1 < 3 **and** 2 < 5) produces the value **True** because both conditions are true.  If one condition is false, then the value produced will be **False**.

For example, the code

```python
print(3 > 1 or 2 < 5)
print(1 < 3 and 2 < 5)
```

produces

```
True
True
```

## Using Logical Operators

If you want to test two related conditions in an if/elif statement you could use one of the logical operators **and** or **or**.

For example, let's say we want to determine if **at least one** of two integers is odd.  There are two ways we could write the program,

```python
m = 5
n = 8
if m % 2 != 0:
  print("Odd")
elif n % 2 != 0:
  print("Odd")
else:
  print("Neither one of the values is odd.")
```

or to be more concise we could use the **or** logical operator,

```python
if m % 2 != 0 or n % 2 != 0:
  print("Odd")
else:
  print"Neither one of the values is odd.")
```

If we wanted to determine if **both integers** are odd, we could use the **and** logical operator,

```python
if m % 2 != 0 and n % 2 != 0:
  print("Both Odd")
else:
  print"One of the numbers is even.")
```
