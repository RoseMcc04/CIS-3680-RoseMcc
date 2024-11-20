# Basic Classes

## Table of Contents

0. [Table of Contents](#table-of-contents)
1. [Getting Inside Objects and Classes](#getting-inside-objects-and-classes)
2. [*Example: The Student Class*](#example-the-student-class)
3. [Docstrings](#docstrings)
4. [Method Definitions](#method-definitions)
5. [The `__init__` Method and Instance Variables](#the-__init__-method-and-instance-variables)
6. [The `__str__` Method](#the-__str__-method)
7. [Accessors and Mutators](#accessors-and-mutators)
8. [Other Special Methods](#other-special-methods)
9. [Rules of Thumb for Defining a Simple Class](#rules-of-thumb-for-defining-a-simple-class)

## Objectives

- Examine the use of basic classes
- Explain the creation of a basic class
- Understand different method types

## Getting Inside Objects and Classes

- Programmers who use objects and classes know:
    - The interface that can be used with a class
    - The state of an object
    - How to instantiate a class to obtain an object
- Objects are abstractions
    - Package their state and methods in a single entity used to maintain the state of an object
- Class definition is like a blueprint for each of the objects of that class and cintains:
    - Definitions of all of the methods that its objects recognize
    - Descriptions of the data structures used to maintain the state of an object

## *Example: The Student Class*

- A course management application needs to represent information about students in a course
```shell
>>> from student import Student
>>> s = Student(“Maria”, 5)
>>> print(s)
Name: Maria
Scores: 0 0 0 0 0
>>> s.setScore(1, 100)
>>> print(s)
Name: Maria
Scores: 100 0 0 0 0
>>> s.getHighScore()
100
>>> s.getAverage()
20
>>> s.getScore(1)
100
>>> s.getName()
'Maria'
```
| **Student Method**   | **What It Does**                                                                                     |
|-----------------------|-----------------------------------------------------------------------------------------------------|
| `s = Student(name, number)` | Returns a Student object with the given name and number of scores. Each score is initially 0. |
| `s.getName()`         | Returns the student’s name.                                                                         |
| `s.getScore(i)`       | Returns the student’s ith score; `i` must range from 1 through the number of scores.                |
| `s.setScore(i, score)`| Resets the student’s ith score to `score`. `i` must range from 1 through the number of scores.       |
| `s.getAverage()`      | Returns the student’s average score.                                                                |
| `s.getHighScore()`    | Returns the student’s highest score.                                                                |
| `s.__str__()`         | Same as `str(s)`. Returns a string representation of the student’s information.                     |
- Syntax of a simple class definition:
```text
class <class name>(<parent class name>):
    <method def-1>
    ...
    <method def-n>
```
- Class is a Python identifier
    - Typically capitalized
- Python classes are organized in a tree-like class hierarchy
    - At the top, or root, of this tree is the object class
    - Some terminology: subclass, parent class/superclass


## Docstrings

- Docstrings can appear at three levels:
    - Module
    - Just after class header
        - To describe its purpose
    - After each method header
        - Serve same role as tehy do for function definitions

## Method Definitions

- Method definitions are indented below class header
- Syntax of method definitions similar to functions
    - Can have required and/or default arguments, return values, create/use temporary variables
    - Returns **None** when no return statement is used
- Each method definition must include a first parameter called **self**    

## The `__init__` Method and Instance Variables

## The `__str__` Method

## Accessors and Mutators

## Other Special Methods

## Rules of Thumb for Defining a Simple Class
