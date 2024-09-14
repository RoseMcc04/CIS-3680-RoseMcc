# Selection Statements

## Table of Contents

0. [Table of Contents](#table-of-contents)
1. [Objectives](#objectives)
2. [If and Else-If Statements](#if-and-else-if-statements)
3. [The Process](#the-process)
4. [One-Way Selection Statements](#one-way-selection-statements)
5. [If-Else Statements](#if-else-statements)
6. [Multi-Condition Selection Statements](#multi-condition-selection-statements)
7. [Compound Boolean Expressions](#compound-boolean-expressions)
8. [Logical Operator Precedence](#logical-operator-precedence)
9. [Short-Circuit Evaluation](#short-circuit-evaluation)
10. [Testing Selection Statements](#testing-selection-statements)

## Objectives

- Explain the Boolean data type
- Explain the variations of the if statement
- Understand how compound Boolean expressions work 

## If and Else-If Statements

- **Selection Statement**
    - allows a computer to make choices based on a **condition**
```python
if x > 1:
    return True
else:
    return False
```

## The Process

- The **Boolean** data type consists of two values:
    - **True** and **False**
- Comparison Operators produce a Boolean result
- **Boolean expression**
    - expression that evaluates to True or False
    - *Example: 4 != 4 evaluates to False*

## One-Way Selection Statements

- Simplest form of selection is the if statement
```text
if <condition>:
    <sequence of statements>
```
- **Example**
```python
while x <= 100:
    if x > 10:
        print("Scaling x")
        x /= 10
```

## If-Else Statements

- Also called a two-way selection statement
- Often used to check inputs for errors
```python
import math
area = float(input("Enter the area: "))
if area > 0:
    radius = math.sqrt(area / math.pi)
    print(f"The area is {radius}.")
else:
    print("Error: the area must be a positive number")
```

## Multi-Condition Selection Statements

- A program may be faced with testing conditions that entail more than two alternative courses of action
- Can be described in code with a **multi-condition selection statement**
- **Example**
```python
number = int(input("Enter the numeric grade: "))
if number > 89:
    letter = 'A'
elif number > 79:
    letter = 'B'
elif number > 69:
    letter = 'C'
elif number > 59:
    letter = 'D'
else:
    letter = 'F'
print("The letter grade is " + letter + ".")
```
- **Syntax**
```text
if <condition-1>:
    <sequence of statements-1>
elif <condition-n>:
    <sequence of statements-n>
else:
    <default sequence of statements>
```

## Compound Boolean Expressions

- Often a course of action must be taken if either of two conditions are true
```python
number = int(input("Enter the numeric grade: "))
if number > 100 or number < 0:
    print("Error: grade must be between 100 and 0")
else:
    print("This is a real grade")
```
- Verifying truth tables
```shell
>>> A = True
>>> B = False
>>> A and B
False
>>> A or B
True
>>> not A
False
```
- The logical operators are evaluated after comparisons but before the assignment operator
    - **not** has higher precedence than **and** and **or**

## Logical Operator Precedence

| **Operation**              | **Symbol(s)**                |
|----------------------------|------------------------------|
| Exponentiation              | `**`                         |
| Arithmetic negation         | `-`                          |
| Multiplication, division, remainder | `*`, `/`, `%`        |
| Addition, subtraction       | `+`, `−`                     |
| Comparison                  | `==`, `!=`, `<`, `>`, `<=`, `>=` |
| Logical negation            | `not`                        |
| Logical conjunction         | `and`                        |
| Logical disjunction         | `or`                         |
| Assignment                  | `=`                          |

## Short-Circuit Evaluation

## Testing Selection Statements