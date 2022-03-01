# Working with Strings

**Strings** consist of a **sequence** of **characters**. Each character is accessed using an **index** value. For example,

```python
word = "chicken"
print( word[0] )
print( word[4] )
```

produces the output,

```
c
k
```

Here is how the **string** stored with the variable / identifier **word** is stored

| **0** | **1** | **2** | **3** | **4** | **5** | **6** |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| c | h | i | c | k | e | n |

Notice the index values begin with the value 0, and indicate the position of each character in the string.

## **The Function len\(\)**

The function **len\(\)** calculates the length of the string \(how many characters are in the sequence\). In the example above,

**len\( word \)** has a value of **7**. For example,

```python
print( len( word ) )
```

**produces the output …**

```
7
```

## **Slices of a String**

```python
word = "chicken"
```

Sometimes you may want to select portions of a string called a **slice**. For example:

```python
print( word[0:3] )
```

produces the output

```
chi
```

The slice of the string consists of the characters from index 0 to 3 \(not including 3\).

```python
print( word[:3] )
```

produces the same output

```
chi
```

If the first index is missing, it is assumed the slice begins at the first character in the string. Similarly,

```python
print( word[3:6] )
```

produces the output

```
cke
```

The slice of the string consists of the characters from index 3 to 6 \(not including 6\). Whereas,

```python
print( word[3:] )
```

produces the output

```
cken
```

If the second index is missing, it is assumed the slice ends after the last character in the string. Adding a third number, allows you to step through the string with any size step. For example,

```python
print( word[::2] )
```

produces the output

```
cikn
```

The slice starts at the beginning of the string and passes through in steps of 2 to just after the end of the string. This can be used to ** easily reverse a string ** as follows,

```python
print( word[::-1] )
```

produces the output

```
nekcihc
```

In this case the first number is assumed to be the final position in the string, and the second just before the first position. Similarly,

```python
print( word[5:2:-1] )
```

produces the output

```
ekc
```

The slice of the string consists of the characters from index 5 to 2 \(not including 2\).

## String Methods

To count the number of occurrences of a character or substring within a string, you can use the **count** method.

For example:

```python
school = "Albert College"
print(school.count('e'))
```

produces the output

```
3
```

The method **count** returns an integer value that can be output or saved to a variable.  

For example:

```python
animal = "massasauga rattlesnake"
numberOfA = animal.count('a')
print(numberOfA)
```

produces the output

```
6
```

What do you think we could count if we wanted to determine the number of words in a string?

Sometimes we want to **replace** a character or a substring within a string.  To do so, we can use the **replace** method.

For example:

```python
age = "I am 49 years old."
print(age.replace("old", "young")
```

produces the output

```
I am 49 years young.
```

If we wanted to save the new string and then output it, we could do so like this,

```python
newString = age.replace("old", "young")
print(newString)
```

If you want to find out what other methods can act on strings (such as upper, lower, capitalize, etc.) you can find them [here](https://docs.python.org/3/library/stdtypes.html#string-methods), or just search for "Python 3 String Methods" with your favourite browser.


## Using a for-loop with Strings

There are two ways a loop can be used with strings in Python.

```python
for ch in word:
   print( ch, end = " ")
```

**produces the output …**

```
c h i c k e n
```

where the variable **ch** stores each character of the string during each iteration of the loop.

```python
for i in range(len(word) ):
    print( word[i] , end = " ")
```

**produces the output …**

```
c h i c k e n
```

where the variable **i** stores the index values 0, 1, 2, 3, 4, 5, 6 during each iteration of the loop.

## **Constructing a String Character-by-Character**

You can construct a string by **concatenation**\(adding\) using a **for-loop** and an assignment statement. For example,

```python
word = ""
# called an empty string 
for i in range(3):
    letter =input("Enter a letter: ")
    word = word + letter
print( word )
```

This python program could be run as follows:

```
Enter a letter: a
Enter a letter: b
Enter a letter: c
abc
```

This type of program is necessary in the game called **Hangman** \( a.k.a. Secret Word\), so that the program can store each version of the secret word being guessed. For example,

```python
secretWord = "chicken"
oldWord = "_______"
for j in range(2):
    letter =input("Guess a letter: ")
    newWord = ""
    for i in range(len(secretWord) ):
        if letter == secretWord[i]:
            newWord = newWord + letter
        else:
            newWord = newWord + oldWord[i]
    oldWord = newWord
    for ch in newWord:
        print( ch, end = " ")
        print()
```

This python program could be run as follows:

```
Guess a letter: c
c _ _ c _ _ _
Guess a letter: n
c _ _ c _ _ n
```

## [Python f-Strings](#f-strings)

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

### Formatted output with f-strings

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