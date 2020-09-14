# Mathematics in Python

## Types of Numbers

We're going to look at two types of numbers that we many encounter this year using Python:  integer, and floating-point values.  Notice below that we can use the **_type()_** function to indicate the data type of the given values.

```python
>>> type(5)
<class 'int'>
```

```python
>>> type(3.0)
<class 'float'>
```

### Operations

Look at how the results of addition and subtraction operations compare when using different types of numbers.

```python
>>> 7 - 10
-3
>>> 5.0 + 1.3
6.3
>>> 6.5 - 4
2.5
>>> 5 / 3
1.6666666666666667
>>> 2**3
8
>>> 7 - 10 + 5*2**3
37
```

##### Integer Division
Sometimes you only want to calculate the integer part of a division operation.  You accomplish this by using the integer division operator **//**.

```python
>>> 5 // 3
1
```

##### Modulus _(Remainder)_
The modulus or remainder operator calculates the remainder of a division operation.  So, **a % b** calculates the remainder of **a / b**.

```python
>>> 5 % 3
1
```

## Exercises

1. How many seconds are there in 13 minutes and 13 seconds?

2. How many miles are in 10 kilometers? _(1 mile is 1.61 kilometers)_

3. How many minutes and seconds are there in 1423 seconds?

4. If you run 10 kilometers in 33 minutes and 14 seconds,

		a. What is your average time per mile in minutes and seconds?
		b. What is your average speed in miles per hour?
    
5. The **volume** of a **sphere** with a radius **r** is 
<img src="https://render.githubusercontent.com/render/math?math=\frac{4}{3} \pi r^3">.  What is the **volume** of a **sphere** with a radius of 5 ?

6.  Given a right angled triangle with side lengths **a = 5** and **b = 9**, calculate the _hypotenuse_ **c**

