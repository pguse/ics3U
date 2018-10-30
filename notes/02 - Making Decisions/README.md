# Making Decisions

All programs have been executed sequentially, line by line, up to this point.  Often programs need to make decisions based on certain conditions determined by the value of a variable.  In Python, decisions are made using the if / elif /else statement.

## Comparison Operators

These statements require that you use one of a number of comparison operators.  For example,

* \<   ***(less than)*** the condition is true if left side is less than right side. 
* \>   ***(greater than)*** the condition is true if left side is greater than right side. 
* \<\=  ***(less than or equal)***
* \>\=  ***(greater than or equal)***
* \=\=  ***(equal to)***
* \!\=  ***(not equal to)***


## Boolean Values & Logical Operators

All **if/elif/else** statements use **Boolean** values, even though that may not be apparent.  For example,

* print( 3 > 1) produces the value **True**
* print( 2 < 5 ) produces the value **False**.

The values **True** and **False** are called **Boolean** values.

If you need to test more than one condition you may need to use a **logical operator**.  In Python, the logical operators are the keywords **and** and **or**.  For example,

* print( 3 > 1 **or** 2 < 5) produces the value **True** because one of the conditions is true.  Both conditions must be false to produce the value **False**.
* print( 1 < 3 **and** 2 < 5) produces the value **True** because both conditions are true.  If one condition is false, then the value produced will be **False**.
