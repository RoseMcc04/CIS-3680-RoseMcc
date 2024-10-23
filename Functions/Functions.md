# Functions

## Table of Contents

0. [Table of Contents](#table-of-contents)
1. [Objectives](#objectives)
2. [Overview of Functions](#overview-of-functions)
3. [Improved Code with Functions](#improved-code-with-functions)
4. [Basic Function Syntax](#basic-function-syntax)
5. [Parameters and Arguments](#parameters-and-arguments)
6. [The Return Statement](#the-return-statement)
7. [Boolean Functions](#boolean-functions)
8. [Defining a Main Function](#defining-a-main-function)
    1. [Main Function Example](#main-function-example)

## Objectives

- Discuss the use of functions
- Explain how to define a function
- Examine several uses of functions

## Overview of Functions

- A function packages an algorithm into a chunk of code that you can call by a function name
- A function can be called from anywhere in a program's code, including code within other functions
- A function can receive data from its caller called arguments
- When a function is called, any expression supplied as arguments are first evaluated
- A function may have one or more **return** statements

## Improved Code with Functions

- Eliminate redundant, or repetitious, code
- Serve as Abstraction Mechanisms
    - Hides detail - Allows a person to view many things as just one thing
    - A function call expresses the idea of a process to the programmer
- Allows us to organize our code more effectively
- Make code reusable

## Basic Function Syntax

- Definition of a function consists of a header and a body
```python
def square(x):
    """Returns the square of x."""
    return x ** 2
```
- Docstring contains information about what the function does; to display, enter **`help(square)`**
- A function can be defined in a Python shell, but it is more convenient to define it in an IDE window
- Syntax of a function definition: 
```text
def <function name>(<parameter-1>,...,<parameter-n>):
    <body>
```

## Parameters and Arguments

- A paramter is the name used in the function definition for an argument that is passed to the function when it is called
- For now, the number and positions of arguments of a function call should match the number and positions of the paramters in the definition
- Some function expect no arguments
    - They are defined with no parameters

## The Return Statement

## Boolean Functions

## Defining a Main Function

### Main Function Example
