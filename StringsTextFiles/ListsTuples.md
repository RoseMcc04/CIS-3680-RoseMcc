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

The **list** type includes several methods for working with elements

| List Method              | What It Does                                                                                     |
|--------------------------|--------------------------------------------------------------------------------------------------|
| `myList.append(element)` | Adds `element` to the end of `myList`                                                            |
| `myList.extend(aList)`   | Adds the elements of `aList` to the end of `myList`                                              |
| `myList.insert(index, element)` | Inserts `element` at `index`. If `index` is less than the length of `myList`, `element` is inserted at `index`. Otherwise, `element` is added to the end of `myList`. |
| `myList.pop()`           | Removes and returns the element at the end of `myList`                                           |
| `myList.pop(index)`      | Removes and returns the element at `index` in `myList`                                           |

## Searching a List

- **`in`** determines an element's presence or absence, but does 
not return position of element (if found)
- Use method `index()` to locate an element's position in a list
    - Raises an error when the target element is not found 
```python
mylist = [34, 45, 67]
target = 45
if target in mylist:
    print(mylist.index(target))
else:
    print(-1)
```

## Sorting a List

- The method **sort()** mutates a list by arranging its elements 
in ascending order 
```shell
>>> mylist = [4, 2, 10, 8]
>>> mylist 
[4, 2, 10, 8]
>>> mylist.sort()
>>> mylist 
[2, 4, 8, 10]
```
- When the elements can be related by comparing them with `<`, `>`, 
and `==`, they can be sorted

## Mutator Methods and the Value `None`

- All the functions and method examined previously return a value 
that the caller can then use to complete its work 
- **Mutator** methods (e.g. insert, appedn, extend, pop, and sort)
usually return no value of interest to the caller
    - Python automatically returns the special value **`None`**
```shell
>>> mylist = mylist.sort()
>>> print(mylist)
None 
```

## Tuples

- A tuple resembles a list, but is immutable
- Indicate by enclosing its elements in parentheses
```shell
>>> fruits = ("apple", "banana")
>>> fruits 
('apple', 'banana')
>>> meats = ("fish", "poultry")
meats 
('fish', 'poultry')
>>> food = meats + fruits
>>> food
('fish', 'poultry', 'apple', 'banana')
>>> veggies = ["celery", "beans"]
>>> tuple(veggies)
('celery', 'beans')
```
