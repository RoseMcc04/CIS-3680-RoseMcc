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
- In Python, all classes automatically extend the built-in object class
- It is possible to extend any existing class:
```text
class <new class name>(<existing parent class name>):
```
- *Example*:
    - ***PhysicalObject** would extend **object***
- Inheritance hierarchies provide an abstraction mechanism that allows the programmer to avoid reinventing the wheel or writing redundant code

## *Example: A Restricted Savings Account*

```shell
>>> account = RestrictedSavingsAccount("Ken", "1001", 500.00)
>>> print(account)
Name: Ken
PIN: 1001
Balance: 500.0
>>> account.getBalance()
500.0
>>> for count in range(3):
account.withdraw(100)
>>> account.withdraw(50)
‘No more withdrawals this month’
>>> account.resetCounter()
>>> account.withdraw(50)
```
- To call a method in the parent class from within a method with the same name in a subclass:
```text
<parent class name>.<method name>(self, <other arguments>)
```

## *Example: The Dealer and a Player in the Game of Blackjack*

- An object belonging to Blckjack class sets up the game and manages the interaction with the user
```shell
>>> from blackjack import Blackjack
>>> game = Blackjack()
>>> game.play()
Player:
2 of Spades, 5 of Spades
7 points Dealer:
5 of Hearts
Do you want a hit? [y/n]: y
Player:
2 of Spades, 5 of Spades, King of Hearts
17 points
Do you want a hit? [y/n]: n
Dealer:
5 of Hearts, Queen of Hearts, 7 of Diamonds
22 points
Dealer busts and you win
```

## Polymorphic Methods

## Costs and Benefits of Object-Oriented Programming
