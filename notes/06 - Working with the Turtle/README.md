# Working with the Turtle

A computer program is just a series of **instructions** given to a computer to perform.  Here is an example of a program in Python that uses the turtle module.

```python
import turtle

# Initialize the turtle object

# Creating a turtle object as defined in the turtle module imported above

tina = turtle.Turtle()

# Turtle objects have associated functions that either set properties of the turtle or move the turtle.
# Here we set three turtle properties

tina.shape('turtle')
tina.width(2)
tina.color('blue')

# Create the turtle functions

# Definition of the square() function
# Instructs the turtle how to draw a square

def square():
  tina.forward(100)
  tina.right(90)
  tina.forward(100)
  tina.right(90)
  tina.forward(100)
  tina.right(90)
  tina.forward(100)
  tina.right(90)

square()
```

The act of creating a function follows an important guiding principle in programming, **Don't Repeat Yourself**.  A function enables you to reuse code by assigning a name to it, instead of re-typing all the lines the next time you need to use it.

In our **square()** function above, you can see that we have a repetition of code happening within the function.  The lines

```python
tina.forward(100)
tina.right(90)
```
occur four times.  A better version of the square function would use a **for-loop** as follows:

```python
def square():
    for i in range(4):
        tina.forward(100)
        tina.right(90)
```

Notice that all lines contained within a **function** must be ***indented*** in Python, as they must be when they are within a **for-loop**.

## Using Parameters with Functions

You can provide input to a function that enables it to be more flexible.  For example, providing the **parameter** s to the **square()** function enables you to modify the side length of the drawn square.  For example, the following code will draw a square of side length 50.

```python
def square(s):
    for i in range(4):
        tina.forward(s)
        tina.right(90)

square(50)
```
More than one parameter can be provided to functions by separating them with commas.

## Notes:

* To use the turtle module it must first be imported as done on the first line using the **import** command.
* All lines beginning with **\#** are comments.  _These are not read by the Python interpreter._
* All instructions are performed line by line from top to bottom
* The variable **tina** is an example of an **object** \(of type Turtle\).  The turtle module provides different **properties** that can be set for turtle objects.  For example:  shape, width, and color.  Notice the use of the **dot** \(operator\) when assigning these properties.  The turtle module also provides different **methods**/actions that the turtle can perform.  For example: forward, and right.  Again, notice the use of the **dot** when implementing these **methods**.
* The line **def** square\(\) gives a name to our sequence of instructions that move the turtle.  In order to run these instructions, we must type square\(\) ... this is called a **function** in Python.  The line **def** square\(\) simply defines the function, whereas the line square\(\) actually runs the instructions contained within the function.
