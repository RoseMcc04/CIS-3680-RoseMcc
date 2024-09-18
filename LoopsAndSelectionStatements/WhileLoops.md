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
- *Example:*
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

- The **while** loop can be complicated to write correctly. However, it is possible to simplify its structure and improve its readibility
```python
total = 0.0
while True:
    data = input("Enter a number or just enter to quit: ")
    if data = "":
        break
    number = float(data)
    total += number
print(f"The sum is {total}.")
```
- Within this body, the input datum is received, then tested for the loop's **termination condition** in a one-way selection statement
- The **break** statement will cause an exit from the loop
- *Example: Using a Boolean variable to control the loop*
```python
done = False
while not done:
    number = int(input("Enter the numeric grade: "))
    if number >= 0 and number <= 100:
        done = True
    else:
        print("Error: grade must be between = and 100.")
print(number) # Echo the valid input
```

## Loop Logic, Errors, and Testing

## Using Random Numbers

## Augmented Assignment

## Simple Guessing Game Script