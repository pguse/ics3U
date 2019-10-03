# Repetition

## The for-loop

This type of loop is useful when you know how many times to repeat your instructions. For example.

```python
for i in range(3):
    print “Hello everyone!”
print “Loop finished.”
```

produces the output:

```
Hello everyone!
Hello everyone!
Hello everyone!
Loop finished
```

The function **range**\(3\) causes the loop to repeat 3 times. Changing it to **range**\(5\) would repeat the loop 5 times. The variable **i** takes on the values 0, 1, and 2 during each repetition of the loop. For example,

```python
for i in range(3):
    print str(i) +“. Hello everyone!”
```

produces the output:

```
0. Hello everyone!
1. Hello everyone!
2. Hello everyone!
```

The **range**\(3\) function can be modified in the following ways:

```python
for i in range(1,4):
    print str(i) +“. Hello everyone!”
```

produces the output:

```
1. Hello everyone!
2. Hello everyone!
3. Hello everyone!
```

Notice how the variable **i** now starts at a value of 1 but only goes up to the maximum value \(in this case 4\) but does not take on a value of 4. Also,

```python
for i in range(1,7,2):
    print str(i) +“. Hello everyone!”
```

produces the output:

```
1. Hello everyone!
3. Hello everyone!
5. Hello everyone!
```

In this case, the variable **i** takes on values in steps of 2. We can also count backwards by doing the following:

```python
for i in range(4,1,-1):
    print str(i) +“. Hello everyone!”
```

produces the output:

```
4. Hello everyone!
3. Hello everyone!
2. Hello everyone!
```

Again, the variable **i** does not take on the minimum value of 1, but only goes down to it.

## The for-loop - Using an Accumulator

An accumulator is a variable that is used in a loop to construct a value using an iterative process.  It could act like a counter using addition, or perform exponentiation through repeated multiplication, or build a string character by character.  Here is an example of an accumulator in action.

### The Sum of all Integers

The act of adding consecutive integers e.g. 0 + 1 + 2 + 3 + 4 + 5 + ... can be thought of as an iterative process.  In each step you are adding ... the only thing that changes is the number being added.  In Python, this can be done using a loop, as follows:

```python
N = 5
s = 0
for i in range(1, N+1):
    s = s + i
print s
```

The result \(15\) that is printed is the sum of all integers between 1 and 5.  Here is a table that summarizes how each variable changes values are the loop iterates.

| N | i | s |
| :---: | :---: | :---: |
| 10 | - | 0 |
| 10 | 1 | **1** |
| 10 | **2** | **3** |
| 10 | 3 | 6 |
| 10 | 4 | 10 |
| 10 | 5 | 15 |

The assignment statement **s = s + i** is the key line and most importantly it is read from **right-to-left**.  The current values of **s** and **i** are added together and the result stored back in the variable/identifier called **s**.  In the table above one of these calculations is shown using the bolded values, where **i** and **sum** have the values 2 and 1.  They are added to give the new value of **s**, which is 3.

## The for-loop - without the range\(\) function:

The **for-loop** can be used without the **range**\(\) function in a couple ways. It can be used to pass through the characters in a string as follows:

```python
name =“Ada”
for ch in name:
    print( ch )
```

produces the output:

```
A
d
a
```

It can also be used to pass through the items in a **list** as follows:

```python
names = [“Ada”, “Python”, “Pyret”]
for language in names:
    print language
```

produces the output:

```
Ada
Python
Pyret
```

## The while-loop

The **while-loop** is used when you don't know the exact number of times that a loop needs to repeat.  It only repeats as long as a given condition is true.  Here is an example, where the loop will end only when the user enters a negative value.

```python
n = 1
while n > 0:
  n = input("Enter a number: ")
```

Here is an example of a **while-loop** that will end when the user enters a 'secret' number.

```python
secret = 42
guess = -1
while guess != secret:
    guess = int( input("Guess the secret number: ") )
```

You can write a **while-loop** to repeat a fixed number of times by using an **accumulator** variable \(counter\).  This is similar to how a **for-loop** works.

```python
counter = 1
while counter <= 10:
    print("Hello")
    counter = counter + 1
```

This code will produce the following output.

```
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
```



