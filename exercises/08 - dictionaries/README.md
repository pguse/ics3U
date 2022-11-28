# Dictionaries

Lists are a data structure that allow you to store multiple values using one assigned name.  Read this [note](https://github.com/pguse/ics3u-python/tree/master/notes/11%20-%20Dictionaries) for an introduction to lists.

## Exercises:

Using **Visual Studio Code**, complete the following programs in a folder called **Dictionaries**.

## 08-0: Student Average
Create a file called **average.py**. Write a program with the following specifications:
Given a dictionary containing courses and marks _(see starter code - dict01.py)_, output the average of the marks.

### Example:

```
Given dictionary:

courses = { "Math" : 75, "English" : 90, "History" : 85, "French" : 70, "Geography" : 80, "Science" : 95}

Output:

Average: 82.5
```

## 08-1:  Number of Vowels

Modify the starter code called **number_vowels.py** so that it counts the **number of vowels** found in a text file called **emma.txt** .  You will need to save the text file **emma.txt** in the same folder as **numberVowels.py**.

## 08-2: Letter Count
Create a file called **letter_count.py**. Write a program with the following specifications:
Given a string input by the user, create and fill a dictionary with letters and their frequencies _(how many times does the letter occur in the string?)_.  Output the results as a frequency table.

### Example:

```
Text:  albert college

Output:

a:  1
l:  3
e:  3
r:  1
t:  1
c:  1
o:  1
g:  1
```

## 08-3:  Number of Nucleotides

The genetic language of every living thing on the planet is DNA. DNA is a large molecule that is built from an extremely long sequence of individual elements called nucleotides. 4 types exist in DNA and these differ only slightly and can be represented as the following symbols: **A** for adenine, **C** for cytosine, **G** for guanine, and **T** for thymine."

Given a single stranded DNA string, compute how many times each nucleotide occurs in the string.

In the starter code, **dna.py**, modify the function called **number_nucleotides(strand)** that returns a dictionary with keys that are the nucleotides:  **'A'**, **'C'**, **'G'**, and **'T'** and values that represent **how many times each nucleotide occurs** in a string called **strand**.

## 08-4: Provinces and Territories
Create a file called **provinces_quiz.py**. Write a program that acts the same as your provinces and territories quiz created earlier.  Instead of storing the questions and answers using separate lists, **use a single dictionary**. Be sure to copy the file **provinces.csv** into the same folder as your **Python** file.  **Challenge:** How will you prevent repeated questions?

### Example:

```
What is the capital of Ontario? Toronto
```