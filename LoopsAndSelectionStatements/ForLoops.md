# For Loops

## Table of Contents
0. [Table of Contents](#table-of-contents)
1. [Prerequisites](#prerequisites)
2. [Execute a Statement a Finite Number of Times](#execute-a-statement-a-finite-number-of-times)
3. [Count-Controlled Loops](#count-controlled-loops)
4. [Loop Errors: Off-by-One Error](#loop-errors-off-by-one-error)
5. [Traversing the Contents of a Data Sequence](#traversing-the-contents-of-a-data-sequence)
6. [Specifying the Steps in the Range](#specifying-the-steps-in-the-range)
7. [Count Down Loops](#count-down-loops)
8. [Old-School Formatting Text for Output](#old-school-formatting-text-for-output)
9. [Newer Style Formatting Output](#newer-style-formatting-output)
10. [The f-string...](#the-f-string)

## Objectives

- Understand for-loops
- Discuss formatting output

## Prerequisites

- While loops
- Basic print function

## Execute a Statement a Finite Number of Times

- Python's for-loop is the control statement that most easily supports finite iteration
```shell
>>> for each_pass in range(4):
...    print("It's alive!", end = " ")
>>> It's alive! It's alive! It's alive!
```
- The form of this type of loop is:
```text
for <variable> in range(<an integer expression>):
    <statement-1>

    <statement-n>
```
- First line of code is sometimes called the loop header
- The rest of the code is the loop body (must be indented and aligned in the same column)
- *Example: Loop to compute an exponentiation for a non-negative exponent*
```shell
>>> number = 2
>>> exponent = 3
>>> product = 1
>>> for each_pass in range(exponent):
        product *= number
        print(product, end = " ")
2 4 8
>>> product
8
```
- If the exponent were 0, the loop body would not execute and the value of the product would remain as 1

## Count-Controlled Loops

## Loop Errors: Off-by-One Error

## Traversing the Contents of a Data Sequence

## Specifying the Steps in the Range

## Count Down Loops

## Old-School Formatting Text for Output

## Newer Style Formatting Output

## The f-string...