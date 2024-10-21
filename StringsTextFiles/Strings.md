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

## Slicing for Substrings

## Testing for Substrings with the `in` Operator

## String Methods

