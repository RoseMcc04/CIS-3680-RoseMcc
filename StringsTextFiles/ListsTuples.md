# Lists and Tuples

## Table of Contents

0. [Table of Contents](#table-of-contents)
1. [Objectives](#objectives)
2. [Lists](#lists)
3. [List Literals](#list-literals)
4. [`list()` Function](#list-function)
5. [Basic List Operators](#basic-list-operators)
6. [Replacing an Element in a List](#replacing-an-element-in-a-list)
7. [List Methods](#list-methods)
8. [Searching a List](#searching-a-list)
9. [Sorting a List](#sorting-a-list)
10. [Mutator Methods and the Value `None`](#mutator-methods-and-the-value-none)
11. [Aliasing and Side Effects](#aliasing-and-side-effects)
12. [Object Identity and Structural Equivalence](#object-identity-and-structural-equivalence)
13. [Tuples](#tuples)

## Objectives

- Explain and explore the list data type
- Explain the tuple data type

## Lists

- Sequence of data values (**items** or **elements**) separated by commas inside
- Strings enclosed in quotes and numbers without quotes
- A few examples:
    - Shopping list
    - To-do list
    - Roster for an athletic team
    - Guest list for an event
    - Recipe - a list of instructions
    - Text document - a list of lines
- Each item in a list has a unique **index** that specifies its position (from 0 to length - 1)

## List Literals

- Syntax:
    - Square brackets surround the elements contained in the list
    - Commas separate elements
    - Elements are literals or expressions
```python
my_list = ['apples', 'oranges', 'cherries']
my_list = [[5, 9], [541, 78]] # list of lists!
```
- When an element is an expression, its value is included in the list:
```shell
>>> import math
>>> x = 2
>>> [x, math.sqrt(x)]
[2, 1.4142135623730951]
>>> [x + 1]
[3]
```

## `list()` Function

## Basic List Operators

## Replacing an Element in a List

## List Methods

## Searching a List

## Sorting a List

## Mutator Methods and the Value `None`

## Aliasing and Side Effects

## Object Identity and Structural Equivalence

## Tuples
