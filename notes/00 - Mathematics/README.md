# Mathematics in Julia

## Types of Numbers

We're going to look at three types of numbers that we many encounter this year using Julia:  integer, floating-point, and rational values.  Notice below that we can use the **_typeof()_** function to indicate the data type of the given values.

'''python
typeof(5)
'''

### Operations

Look at how the results of addition and subtraction operations compare when using different types of numbers.

##### Integer Division
Sometimes you only want to calculate the integer part of a division operation.  You accomplish this by using the integer division operator **//**.

##### Modulus _(Remainder)_
The modulus or remainder operator calculates the remainder of a division operation.  So, **a % b** calculates the remainder of **a / b**.

## Exercises

1. How many seconds are there in 13 minutes and 13 seconds?

2. How many miles are in 10 kilometers? _(1 mile is 1.61 kilometers)_

3. How many minutes and seconds are there in 1423 seconds?

4. If you run 10 kilometers in 33 minutes and 14 seconds,

		a. What is your average time per mile in minutes and seconds?
		b. What is your average speed in miles per hour?
    
5. The **volume** of a **sphere** with a radius **r** is $$\frac{4}{3} \pi r^3$$.  What is the **volume** of a **sphere** with a radius of $radius ?

6.  Given a right angled triangle with side lengths **a = $a** and **b = $b**, calculate the _hypotenuse_ **c**
