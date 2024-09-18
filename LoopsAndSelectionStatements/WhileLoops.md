# While Loops

## Table of Contents

0. [Table of Contents](#table-of-contents)
1. [Underlying Concept](#underlying-concept)
2. [While-Loop Structure](#while-loop-structure)
3. [Count Control](#count-control)
4. [While-True with Break Statement](#while-true-with-break-statement)
5. [Loop Logic, Errors, and Testing](#loop-logic-errors-and-testing)
6. [Using Random Numbers](#using-random-numbers)
7. [Augmented Assignment](#augmented-assignment)
8. [Simple Guessing Game Script](#simple-guessing-game-script)

## Objectives

- Understand loops
- Define how a loop works
- Explore several ways to implement a while loop
- Identify how to generate random numbers

## Underlying Concept

- Repetition statements (or **loops**) repeat a sequence of operations
- Each repetition is known as a **pass** or **iteration**
- Two basic types of loops:
    - **Definite Iteration**
        - Those that repeat a predefined number of times
    - **Indefinite Iteration**
        - Those that repeat until the program determines it needs to stop

## While-Loop Structure

- The **while** loop can be used to describe conditional iteration
    - *Example: A program's input loop that accepts values until the user enters a **sentinel** value that terminates the input*
- Conditional iteration requires that a condition be tested within the loop to determine if it should continue
    - Called **continuation condition**
- Syntax
```python
while <condition>:
    <sequence of statements>
```
- Improper use may lead to an **infinite loop**
- Also called an **entry-control loop**
    - Condition is tested at top of loop
    - Statements within loop can execute zero or more times
- **Example**
```python
total = 0.0
data = input("Enter a number or just enter to quit: ")
while data != "":
    number = float(data)
    total += number
    data = input("Enter a number or just enter to quit: ")
print(f"The total is {total}.")
```

## Count Control

- Use a **while** loop for a count-controlled loop
```python
# Summation with a while loop
total = 0
count = 1
while count <= 100:
    total += count
    count += 1
print(total)
```

## While-True with Break Statement

## Loop Logic, Errors, and Testing

## Using Random Numbers

## Augmented Assignment

## Simple Guessing Game Script