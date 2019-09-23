# Making Decisions

## Exercises:
Using **Visual Studio Code**, complete the following programs.

## 01-0: Is it Odd?
Create a file called **isOdd.py**.  Create a program with the following specifications: **Input:**  An integer, **Output:** print "YES" if it's odd and print "NO" otherwise.

### For example:
```
Integer: 5
YES
```

## 01-1: At Least One Odd Number?
Create a file called **atLeastOneOdd.py**.  Create a program with following specifications:  **Input:**  two integers, **Output:**  print "YES" if at least one of them is odd and print "NO" otherwise.

### For example:
```
Integer #1: 5
Integer #2: 4
YES
```

## 01-2: Ascending Integers?
Create a file called **ascending.py**.  Create a program with the following specifications:  **Input:** three different integers, **Output:** print YES if they're given in ascending order, print NO otherwise.

### For example:
```
Integer #1: 5
Integer #2: 4
Integer #3: 6
NO
```

## 01-3: How Many Days in a Month?
Create a file called **daysInMonth.py**.  Create a program with the following specifications:  **Input:**  A month - an integer from 1 (January) to 12 (December), **Output:**  print the number of days in it in the year 2019 (or any other non-leap year).

### For example:
```
Month: 5
Days: 31
```

## 01-4: Solve for x
Create a file called **linearEquation.py**.  Create a program that solves a linear equation ax = b, in integers, with the following specifications:  **Input:**  two integers a and b (a may be zero), **Output:**  print a single integer root (solution) if it exists and print "no solution" or "many solutions" otherwise.

### For example:
```
a: 5
b: 30
6
```

```
a: 0
b: 4
no solution
```

```
a: 0
b: 0
many solutions
```

## 01-5: Rook Move
Create a file called **rookMove.py**. Chess rook moves horizontally or vertically. Given two different cells of the chessboard, determine whether a rook can go from the first cell to the second in one move.  The program receives the **input** of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a rook can go from the first cell to the second in one move, or NO otherwise.

![rookMove.png](https://github.com/pguse/ics3u/blob/master/images/rook_move.png)

### For example:
```
Column #1: 5
Row #1: 4
Column #2: 1
Row #2: 4
YES
```

```
Column #1: 5
Row #1: 4
Column #2: 4
Row #2: 5
NO
```

## 01-6: Leap Year
Create a file called **leap.py**. Given the year number. You need to check if this year is a leap year. If it is, print LEAP, otherwise print COMMON.  The rules in Gregorian calendar are as follows:

+ a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100
+ a year is always a leap year if its number is exactly divisible by 400

### For example:
```
Year: 1800
NO
```

```
Year: 1600
YES
```

```
Year: 2020
YES
```
---

***Reference:*** http://snakify.org
