# Python - Getting Started

## Table of Contents

## Objectives

- Become familiar with the interactive shell
- Discuss scripts
- Examine the use of an Integrated Development Environment
- Write a simple Python program
- Discuss finding errors 

## Before we get Started

- Install Python3
- Install Visual Studio Code (VSCode)
- Install VSCode extension in Python

## Background

- **Python** is a high-level, general-purpose programming language for solving problems on modern computer systems
- Invented in 1991 by Guido van Rossum

## Running Code in the Interactive Shell

- Python script: a text file containing Python code passed to an interpreter
- Python is an **interpreted** language: instructs computer to carry out operations described by code
- Simple Python expressions and statements can be run in the **Shell**
    - Useful for:
        - Experimenting with short expressions or statements
        - Consulting the documentation
    - Ways to open a Python shell:
        - Launch a command prompt
        - Launch an Anaconda prompt and run Python
        - Launch the Integrated Development Environment (IDE)
    - To quit:
        - Select the window's close box
        - Press ctrl+D
        - Call the function exit()

## Input, Processing, and Output

- Programs usually accept inputs from a source, process them, and output results to a destination
    - In terminal-based interactive programs, these are the keyboard and terminal display
- In a Python shell, inputs are Python expressions or statements
    - Outputs are the results displayed in the shell
- Programmers can also force output of a value by using the print() function
```python
print(<expression>)
print(<expression>,...,<expression>)        
```
- Example:
```shell
>>>print("Hi there")
Hi there
```
- Example Two:
```shell
>>>first = int(input("Enter the first number: "))
Enter the first number: 23
>>>second = int(input("Enter the second number: "))
Enter the second number: 46
>>>print("The sum is", first + second)
The sum is 69
```
| Function Syntax                       | What It Does                                                                 |
|---------------------------------------|------------------------------------------------------------------------------|
| `float(<a string of digits>)`         | Converts a string of digits to a floating-point value.                        |
| `int(<a string of digits>)`           | Converts a string of digits to an integer value.                              |
| `input(<a string prompt>)`            | Displays the string prompt and waits for keyboard input. Returns the string of characters entered by the user. |
| `print(<expression>, ...,<expression>)`| Evaluates the expressions and displays them, separated by one space, in the console window. |
| `<string 1> + <string 2>`             | Glues the two strings together and returns the result.                        |

