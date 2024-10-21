# Strings

## Table of Contents

0. [Table of Contents](#table-of-contents)
1. [Objectives](#objectives)
2. [Motivation](#motivation)
3. [The Structure of Strings](#the-structure-of-strings)
4. [Escape Sequences](#escape-sequences)
5. [Subscript Operator](#subscript-operator)
6. [Slicing for Substrings](#slicing-for-substrings)
7. [Testing for Substrings with the `in` Operator](#testing-for-substrings-with-the-in-operator)
8. [String Methods](#string-methods)

## Objectives

- Further examining the string data type

## Motivation

- Text -- The Universal Transfer Format
    - Comma Separated Variables (CSV)
    - HTML
    - Text files

## The Structure of Strings

- An integer cannot be factored into more primitive parts
- A string is a **data structure**
    - *Data structure: Consists of smaller pieces of data*
    - *String's length: Number of characters it contains (0+)*
- The **len()** function returns the string's length, which is 
  the number of characters it contains 
```shell
>>> len("Hi there!")
9
>>> len("")
0
```

## Escape Sequences

| Escape Sequence | Meaning                               |
|-----------------|---------------------------------------|
| \\              | Backslash (\)                         |
| \'              | Single quote (')                      |
| \"              | Double quote (")                      |
| \a              | ASCII Bell (BEL)                      |
| \b              | ASCII Backspace (BS)                  |
| \f              | ASCII Formfeed (FF)                   |
| \n              | ASCII Linefeed (LF)                   |
| \r              | ASCII Carriage Return (CR)            |
| \t              | ASCII Horizontal Tab (TAB)            |
| \v              | ASCII Vertical Tab (VT)               |
| \xhh            | ASCII character with hex value hh     |
| \uhhhh          | Unicode character with hex value hhhh |

## Subscript Operator

```shell
>>> name = "Alan Turing"
>>> name[0]
'A'
>>> name[3]
'n'
>>> name[len(name)]
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> name[len(name) - 1]
'g'
>>> name[-1] # Shorthand for the last character
'g'
>>> name[-2] # Shorthand for the next-to-last character
'n'
```
- *Format: <a string>[<an integre expression>]*
- Subscript operator is useful when you want to use the positions as well
  as the characters in a string 
```python
data = "Hi there!"
for index in range(len(data)):
    print(index, data[index])
0 H
1 i
2 
3 t
4 h
5 e
6 r
7 e
8 !
```

## Slicing for Substrings

- Python's subscript operator can be used to obtain a substring through a process
  called **slicing**
- Place a colon `:` in the subscript; an integer value can appear on either side
  of the colon 
```shell
>>> name = "myfile.txt" # The entire string
>>> name[0:]
'myfile.txt'
>>> name[0:1] # The first character
'm'
>>> name[0:2] # The first two characters
'my'
>>> name[:len(name)] # The entire string
'myfile.txt'
>>> name[-3:] # The last three characters
'txt'
>>> name[2:6] # Drill to extract 'file'
'file'
```

## Testing for Substrings with the `in` Operator

## String Methods

