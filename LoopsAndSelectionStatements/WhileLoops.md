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

- Errors to rule out during testing **while** loop:
    - Incorrectly initialized loop control variable
    - Failure to update this variable correctly within loop
    - Failure to test it correctly in continuation condition
- To halt loop that appears to hang during testing, type `CTRL + c` in the terminal window
- If loop must run at least once, use a **while True** loop with delayed examination of termination condition
    - Ensure a **break** statement is reached eventually

## Using Random Numbers

- Programming languages often include resources for generating **random numbers**
    - **randint()** returns a random number from among numbers between two arguments, included
```python
import random
x = 0
while x < 10:
    print(random.randint(1,6), end = " ")
    x += 1
```
Output: 2 4 6 4 2 3 6 2 2

## Augmented Assignment

- The assignment symbol can be combined with the arithmetic and concatenation operators to provide augmented assignment operations
```text
a += 3 --> a = a + 3
a -= 3 --> a = a - 3
a *= 3 --> a = a * 3
a /= 3 --> a = a / 3
a %= 3 --> a = a % 3
s += " there" --> s = s + " there"
```
- Format: <variable> <operator>= <expression>

## Simple Guessing Game Script

```python
import random
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
my_number = random.randint(smaller, larger)
count = 0
while True:
    count += 1
    user_number = int(input("Enter your guess:"))
    if user_number < my_number:
        print("Too small!")
    elif user_number > my_number:
        print("Too large!")
    else:
        print(f"Congratulations! You've got it in {count} tries!")
        break
```