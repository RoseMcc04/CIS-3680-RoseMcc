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

## Compound Boolean Expressions

## Logical Operator Precedence

## Short-Circuit Evaluation

## Testing Selection Statements