# Working with Strings

**Strings** consist of a **sequence** of **characters**. Each character is accessed using an **index** value. For example,

```
word = “chicken”
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

```
print( len( word ) )
```

**produces the output …**

```
7
```

## Using a for-loop with Strings

There are two ways a loop can be used with strings in Python.

```
for ch in word:
   print( ch, end = “ “)
```

**produces the output …**

```
c h i c k e n
```

where the variable **ch** stores each character of the string during each iteration of the loop.

```
for i in range(len(word) ):
    print( word[i] , end = “ “)
```

**produces the output …**

```
c h i c k e n
```

where the variable **i** stores the index values 0, 1, 2, 3, 4, 5, 6 during each iteration of the loop.

## **Constructing a String Character-by-Character**

You can construct a string by **concatenation**\(adding\) using a **for-loop** and an assignment statement. For example,

```
word = “”
# called an empty string 
for i in range(3):
    letter =input(“Enter a letter: “)
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

```
secretWord = “chicken”
oldWord = “_______” 
for j in range(2):
    letter =input( “Guess a letter: “)
    newWord = “”
    for i in range(len(secretWord) ):
        if letter == secretWord[i]:
            newWord = newWord + letter
        else:
            newWord = newWord + oldWord[i]
    oldWord = newWord
    for ch in newWord:
        print( ch, end = “ “)
        print()
```

This python program could be run as follows:

```
Guess a letter: c
c _ _ c _ _ _
Guess a letter: n
c _ _ c _ _ n
```

## **Slices of a String**

```
word = “chicken”
```

Sometimes you may want to select portions of a string called a **slice**. For example:

```
print( word[0:3] )
```

produces the output

```
chi
```

The slice of the string consists of the characters from index 0 to 3 \(not including 3\).

```
print( word[:3] )
```

produces the same output

```
chi
```

If the first index is missing, it is assumed the slice begins at the first character in the string. Similarly,

```
print( word[3:6] )
```

produces the output

```
cke
```

The slice of the string consists of the characters from index 3 to 6 \(not including 6\). Whereas,

```
print( word[3:] )
```

produces the output

```
cken
```

If the second index is missing, it is assumed the slice ends after the last character in the string. Adding a third number, allows you to step through the string with any size step. For example,

```
print( word[::2] )
```

produces the output

```
cikn
```

The slice starts at the beginning of the string and passes through in steps of 2 to just after the end of the string. This can be used to ** easily reverse a string ** as follows,

```
print( word[::-1] )
```

produces the output

```
nekcihc
```

In this case the first number is assumed to be the final position in the string, and the second just before the first position. Similarly,

```
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
print(school.count('e')
```

produces the output

```
3
```

The method **count** returns an integer value that can be output or saved to a variable.  What do you think we could count if we wanted to determine the number of words in a string?

Sometimes we want to replace a character or a substring within a string.  To do so, we can use the **replace** method.

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
new = age.replace("old", "young")
print(new)
```

If you want to find out what other methods can act on strings (such as upper, lower, etc.) you can find them [here](https://docs.python.org/3/library/stdtypes.html#string-methods), or just search for "Python 3 String Methods" with your favourite browser.
