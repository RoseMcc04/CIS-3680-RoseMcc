# Advanced Classes

## Table of Contents

0. [Table of Contents](#table-of-contents)
1. [Objectives](#objectives)
2. [Using pickle for Permanent Storage of Objects](#using-pickle-for-permanent-storage-of-objects)
3. [Input of Objects and the try-except Statement](#input-of-objects-and-the-try-except-statement)
4. [Structuring Classes with Inheritance and Polymorphism](#structuring-classes-with-inheritance-and-polymorphism)
5. [Inheritance Hierarchies and Modeling](#inheritance-hierarchies-and-modeling)
6. [*Example: A Restricted Savings Account*](#example-a-restricted-savings-account)
7. [*Example: The Dealer and a Player in the Game of Blackjack*](#example-the-dealer-and-a-player-in-the-game-of-blackjack)
8. [Polymorphic Methods](#polymorphic-methods)
9. [Costs and Benefits of Object-Oriented Programming](#costs-and-benefits-of-object-oriented-programming)

## Objectives

- Exploit inheritance and polymorphism when developing classes
- Transfer objects to and from files

## Using pickle for Permanent Storage of Objects

- **pickle** allows a programmer to save and load objects using a process called **pickling**
    - Python takes care of all of the conversion details
```python
import pickle

def save(self, fileName = None):
   """Saves pickled accounts to a file. The parameter
   allows the user to change filenames."""
   if fileName != None:
      self.fileName = fileName
   elif self.fileName == None:
      return
   fileObj = open(self.fileName, "wb")
   for account in self.accounts.values():
      pickle.dump(account, fileObj)
   fileObj.close()
```

## Input of Objects and the try-except Statement

```text
try:
    <statement(s)>
except <exception type>:
    <statement(s)>
```
```python
def __init__(self, fileName = None):
     """Creates a new dictionary to hold the accounts.
    If a filename is provided, loads the accounts from
    a file of pickled accounts."""
    self.accounts = {}
    self.fileName = fileName
    if fileName != None:
        fileObj = open(fileName, "rb")
        while True:
	        try:
	            account = pickle.load(fileObj)
	            self.add(account)
	        except EOFError:
 	            fileObj.close()
	            break
```

## Structuring Classes with Inheritance and Polymorphism

- Most object-oriented languages require the programmer to master the following techniques:
    - **Data encapsulation**:
        - Restricting manipulation of an object's state by external users to use a set of method calls
    - **Inheritance**:
        - Allowing a class to automatically reuse and extend code of similar but more general classes
    - **Polymorphism**:
        - Allowing several different classes to use the same general method names
- Python's syntax does not enforce data encapsulation
- Inheritance and polymorphism are built into Python

## Inheritance Hierarchies and Modeling

![Example Image 1](https://www.softwareideas.net/i/DirectImage/1864/Inheritance-in-UML-Class-Diagram)

## *Example: A Restricted Savings Account*

## *Example: The Dealer and a Player in the Game of Blackjack*

## Polymorphic Methods

## Costs and Benefits of Object-Oriented Programming
