# Functions, Modules, and Documenting

## Table of Contents

0. [Table of Contents](#table-of-contents)
1. [Objectives](#objectives)
2. [Functions](#functions)
3. [The Math Module](#the-math-module)
4. [The Main Module](#the-main-module)
5. [Documentation](#documentation)
6. [Comments](#comments)
7. [Extra Advice](#extra-advice)

## Objectives

- Discuss calling functions
- Examine documenting a program
- Define the best way to set up a main module

## Functions

- We have already introduced ourselves to a few casts/functions
    - input()
    - print()
    - int()
    - float()
    - str()
- **Function**
    - a chunk of code that can be called by name to perform a task and only runs when called
- Functions often require data known as **arguments** or **parameters** to be passed to it
    - Arguments may be **optional** or **required**
- When a function completes its task, it may **return a value** back to the program that called it
- To learn how to use a function's argument, use the help function
```shell
>>> help(round)
Help on built-in function round in module builtin:
round(...)
    round(number[, ndigits]) -> floating point number
    Round a number to a given precision in decimal digits (default 0 digits). 
    This returns an int when called with one argument, otherwise the same type as number, ndigits may be negative.  
```
- Python includes many useful functions, which are organized in libraries called **modules**
- [__builtin__ Module](https://docs.python.org/3/library/functions.html)
```shell
>>> final_grade = 75.457
>>> round(final_grade)
75
>>> round(final_grade, 2)
75.46
```

## The Math Module

- **Modules**
    - components of code that include functions and resources
- Functions like **abs()** and **round()** from the `__builtin__` module are <ins>always available to use</ins>
- The **math** module includes functions that perform basic mathematical operations
- To make a module available to your code, you must inport the module
- To use a resources from a module, you write the name of a module as a qualifier, followed by a dot (`.`) and the name of the resource
- *Example*
```shell
>>> import math
>>> math.pi
3.1415926535897931
>>> math.sqrt(2)
1.4142135623730951
```
- You can avoid the use of the qualifier with each reference by importing the individual resources
```shell
>>> from math import pi, sqrt
>>> print(pi, sqrt(2))
3.14159265359 1.41421356237
```
- You may import all of a module's resources to use without the qualifier
    - *This is not a good idea if you can avoid it*
    - *Example: `from math import *`*

## The Main Module

- To differentiate this script from the other modules in a program, we call it the main module
    - Like any other module, the main module can be imported
```shell
>>> import tax_form
Enter the gross income: 120000
Enter the number of dependents: 2
The income tax is $20880.0
```
- After importing a main module, view its documentation by running the help function

## Documentation

## Comments

## Extra Advice
