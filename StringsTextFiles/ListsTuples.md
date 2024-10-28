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

- The list function can build a list from any iterable sequence of elements
```shell
>>> my_list = list("Hi there!")
>>> my_list
['H', 'i', ' ', 't', 'h', 'e', 'r', 'e', '!']
```
- A list of integers can be built using `range()`:
```shell
>>> mylist = [1, 2, 3, 4]
>>> myotherlist = list(range(1, 5))
>>> mylist
[1, 2, 3, 4]
>>> myotherlist
[1, 2, 3, 4]
```

## Basic List Operators

- **len()** works on lists as expected
```shell
>>> len(mylist)
4
>>> mylist[0]
1
>>> mylist[2:4]
[3, 4]
```
- Concatenation `+` and equality `==` also work as expected for lists:
```shell
>>> mylist + [1, 2, 3, 4, 5, 6]
>>> mylist == myotherlist
True
```
- To print the contents of a list:
```shell
>>> print("1234")
1234
>>> print([1, 2, 3, 4])
[1, 2, 3, 4]
```
- **`in`** detects the presence of an element
```shell
>>> 3 in [1, 2, 3]
True
>>> 0 in [1, 2, 3]
False
```

## Replacing an Element in a List

- A list is **mutable**
    - Elements can be inserted, removed, or replaced
    - The list itself maintains its identity, but its **state** - its length and contents - can change
- Subscript operator is used to replace an element
```shell
>>> mylist = [1, 2, 3, 4]
>>> mylist
[1, 2, 3, 4]
>>> mylist[-1] = 0
>>> mylist
[1, 2, 3, 0]
```
- Subscript is used to reference the target of the assignment, which is not the list but an element's position within it
- Examples:
    - *How to replace each number in a list with its square:*
```shell
>>> mylist = [2, 3, 4, 5]
>>> mylist
[2, 3, 4, 5]
>>> for i in range(len(mylist)):
        mylist[i] = mylist[i] ** 2
>>> mylist
[4, 9, 16, 25]
```
    - *Use the string method `split()` to extract a list of words:*
```shell
>>> sentence = "This example has five words."
>>> words = sentence.split()
>>> words
['This', 'example', 'has', 'five', 'words.']
>>> for i in range(len(words)):
        words[i] = words[i].upper()
>>> words
['THIS', 'EXAMPLE', 'HAS', 'FIVE', 'WORDS.']
```

## List Methods

## Searching a List

## Sorting a List

## Mutator Methods and the Value `None`

## Aliasing and Side Effects

## Object Identity and Structural Equivalence

## Tuples
