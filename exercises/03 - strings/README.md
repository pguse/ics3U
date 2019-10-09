# Strings

## Exercises:

Using **Visual Studio Code**, complete the following programs.

## 03-0: Slices
Create a file called **slices.py**.  Write a program with the following specifications:

### Input
* A string
### Output
* In the first line, print the third character of this string.
* In the second line, print the second to last character of this string.
* In the third line, print the first five characters of this string.
* In the fourth line, print all but the last two characters of this string.
* In the fifth line, print all the characters of this string with even indices (remember indexing starts at 0, so the characters are displayed starting with the first).
* In the sixth line, print all the characters of this string with odd indices (i.e. starting with the second character in the string).
* In the seventh line, print all the characters of the string in reverse order.
* In the eighth line, print every second character of the string in reverse order, starting with the last one.
* In the ninth line, print the length of the given string.

### For Example:
```
Enter a string:  Albert College
b
g
Alber
Albert Colle
Abr olg
letClee
egelloC treblA
eelCtel
14
```

## 03-1: Number of Words
Create a file called **numberOfWords.py**.  Write a program with the following specifications:

### Input

* A string consisting of words separated by spaces

### Output

* The number of words the given string has. **Note:**  To solve the problem, use the method **count**.

### For Example:
```
Enter a string:  The quick brown fox jumps over the lazy dog
Number of Words: 9
```

## 03-2: Two Halves
Create a file called **twoHalves.py**.  Write a program with the following specifications:

### Input

* A string

### Output
* Cut it into two "equal" parts ***(If the length of the string is odd, place the center character in the first string, so that the first string contains one more character than the second)***. Now print a new string on a single row with the first and second halfs interchanged ***(second half first and the first half second)***.  Don't use the statement **if** in this task.

### For Example:
```
Enter a string:  Antelope
Two halves reversed: lopeAnte
```

```
Enter a string:  hello
Two halves reversed: lohel
```

### Note:
In order to have the first string be one character longer in the case of an odd length string we need to use the **math** module.  Specifically, we need to use the **math.ceil()** function.  For example, the following code

```python
import math

greeting = "hello"
length = len(greeting)                          # calculates the length of the string ... in this case 5
print( greeting[0: math.ceil( length / 2 )] )
```

will produce the output
```
hel
```

In this case, length / 2 has the value 2.5.  The **math.ceil()** function take a floating-point value and rounds it up to the next highest integer.  So, **math.ceil(2.5)** has the value **3**.  Therefore, the expression **greeting[0: math.ceil( length / 2 )]** is equivalent to **greeting[0:3]**. As an aside, the **math.floor()** function rounds a floating-point value down to the next lowest integer.  So, **math.floor(2.5)** has the value **2**.

## 03-3: Replace 1
Create a file called **replaceOne.py**.  Write a program with the following specifications:

### Input
* A string containing 1's

### Output
* A string with all the number 1's by the word one.

### For Example:
```
Enter a string containing 1's:  1 thousand 1 hundred and twenty 1
Output:  one thousand one hundred and twenty one
```

---
***Reference:*** http://snakify.org
