# Data Types and Variables

## Table of Contents

1. [Objectives](#objectvies)
2. [Memory Storage](#memory-storage)
3. [Data Types](#data-types)

## Objectvies

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
