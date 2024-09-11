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

## The Main Module

## Documentation

## Comments

## Extra Advice
