# Data Types and Variables

## Table of Contents

1. [Objectives](#objectvies)
2. [Memory Storage](#memory-storage)
3. [Data Types](#data-types)
4. [Data Definition](#data-definition)
5. [Built-In Types](#built-in-types)
6. [Data Types - Primary](#data-types---primary)

## Objectives

- Understand how memory works
- Identify what is meant by a data type
- Define the rules and conventions for naming variables
- Understand how variables work in Python

## Memory Storage

- 8 bits = 1 byte
- Stored as 0's and 1's

## Data Types

- Different types of data are stored in different formats
- Different formats take different amounts of memory storage (bytes)
- To work with data, the computer needs to know:
    - The ormat in which the data is stored (unsigned, signed, floating-point, etc.)
    - What operations can be performed on the data (+, -, *, /, etc.)
- This information forms what is called the **Data Type**  

- A **data type** consists of a set of values and a set of operations that can be performed on those values
- A **literal** is the way a value of a data type looks to a programmer

## Data Definition

- **Class**
  - The blueprint of an object
    - Defines attributes (data) and methods (operations) in a "type" of object
- **Object**
    - An *instance* of a class
        - Represents an actual entity/item as defined by a class
    - Comprised of a type, methods, and attributes
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hello(self):
        print(f"Hello, my name is {self.name}.")
```

## Built-in Types

- **Numbers**
    - Integer
    - Float
    - Boolean
    - Complex
    - Decimal
    - Fraction
- **Collections**
    - Sequences
        - Immutable
            - String
            - Bytes
            - Tuple
        - Mutable
            - List
            - Bytearray
    - Mappings
        - Dictionary
    - Sets
        - Set
        - Frozenset
- **Callables**
    - Function
    - Generator
    - Class
    - Method
- **Other**
    - Module
    - Instance
    - File
    - None
    - View
- **Internal**
    - Type
    - Code
    - Frame
    - Traceback

## Data Types - Primary

- **Integers**
    - In real life, the range of **integers** is infinite
    - A computer's memory places a limit on the magnitude of integers
    - Integer literals are written without commas  

- **Floating-Point Numbers**
    - Real numbers have **infinite precision**
    - Python using **floating-point** numbers to *represent* real numbers
    - Python's typical precision is 16 digits
    - A floating-point number can be written using either ordinary **decimal notation** or **scientific notation**
    - Numbers in Python must begin with a numeric digit (0-9), a period (decimal), or a hyphen (negative)  

- **String Literals (Character) Strings**
    - In Python, a string literal is a sequence of characters enclosed in single or double quotation marks
    - `''` and `""` represent the **empty string**
    - Double-quoted strings are handy for composing strings that contain single quotation marks or apostrophes
```shell
>>> "I'm using a single quote in this string!"
"I'm using a single quote in this string!"
>>> print("I'm using a single quote in this string!")
I'm using a single quote in this string!
```  

## Escape Sequences

- The newline character **\n** is called an **escape sequence**

| Escape Sequence | Meaning               | 
|-----------------|-----------------------|
| \b              | Backspace             |
| \n              | Newline               |
| \t              | Horizontal Tab        |
| \\              | The \ character       |
| \'              | Single quotation mark | 
| \"              | Double quotation mark | 
