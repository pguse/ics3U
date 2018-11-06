# Problems of the Week - Part 1

## Exercises:

Using Visual Studio Code, create two programs:  coins.py and guessing.py , according to the specifications given below.

## 03-1:  Coins
Write a program that takes user input : a number of cents, for example 305 cents.
The program will calculate and display the coins that should be used to give that amount of change to a user in coin denominations.
 
### For example :
```
Input the amount in cents:  455

Your change is:
2 Toonies
2 quarters
1 nickel
```

## 03-2: Guessing Game
Write a guessing game that has the user guess a random/secret number between 1 and 100.  After each quess the user is given feedback about their guess:  "Too high"  or "Too low"

### For example:
```
Guess the number:  23

Too low
Guess again: 76
Too high
Guess again: 58
Correct!
```

See the ***starter code*** given in the file **guessStart.py** that contains code that will generate a random number.

## 03-3: Vampire Numbers (OPTIONAL)


What is a Vampire Number?
from MathWorks ...

```
Here is the recipe for rustling up a vampire number. Take any number with an even number of digits. Split that number into two daughter numbers of equal length, which between them comprise all original constituent digits of the first number in any order. If the product of those daughter numbers equals the original number your number is vampiric. In fact, if the daughter numbers satisfy this rule then they are referred to as “fangs”.
```

### Example:

The lowest 4 digit vampire number is 1260, since 1260 = 21 x 60

### Challenge:
Create a program that takes a 4-digit number as input and determines if it is a vampire number.  For example:

#### Input:
```
1260
```
#### Output
```
1260 is a vampire number
```

### Data Representation:
How you choose to represent your data influences your approach to solving a problem.  For example, in this problem representing the original number as a String allows you to easily access the digits.  Look at this example program as a starting point.