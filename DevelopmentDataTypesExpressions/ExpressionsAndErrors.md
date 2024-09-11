# Expressions and Errors

## Table of Contents

1. [Objectives](#objectives)
2. [Like a Workhorse](#like-a-workhorse)
3. [Arithmetic Expressions](#arithmetic-expressions)
4. [Mixed-Mode Arithmetic and Type Casting](#mixed-mode-arithmetic-and-type-casting)
5. [Try-Except Statements](#try-except-statements)
6. [Example](#example)
7. [Handling Multiple Exceptions](#handling-multiple-exceptions)
8. [Raising an Exception](#raising-an-exception)

## Objectives

- Define expressions and their use
- Discuss mixed mode arithmetic and type casting
- Examine exception handling

## Like a Workhorse

- A literal evaluates to itself
- A variable reference evaluates to the variable's current value
- **Expressions** provide an easy way to perform operations on data values to produce other values
- When entered into the Python shell prompt
    - an expression's operands are evaluated
    - its operator is then applied to these values to compute the value of the expression

## Arithmetic Expressions

- Consists of operands and operators combined in a manner that is already familiar from the study of algebra

| Operator | Meaning                | Syntax        |
|----------|------------------------|---------------|
| `**`       | Exponentiation          | `a ** b`   |
| `-`        | Negation                | `-a`       |
| `*`        | Multiplication          | `a * b`    |
| `/`        | Division                | `a / b`    |
| `//`       | Quotient                | `a // b`   |
| `%`        | Remainder or modulus    | `a % b`    |
| `+`        | Addition                | `a + b`    |
| `-`        | Subtraction             | `a - b`    |

- **Precedence Rules**
    - `**` has the highest precedence and is evaluated first
    - Unary negation is evaluated next
    - `*`, `/`, and `%` are evaluated before `+` and `-`
    `-` + and `-` are evaluated before `=`
    - With two exceptions, operations of equal precedence are **left associative**, so they are evaluated from left to right
        - `**` and `=` are **right associative**
    - You can use `()` to change the order of evaluation
```shell
>>> 3 + 4 + 2 ** 3
35
```
- When both operands of an expression are of the same numeric type, the resulting value is also of that type
- When each operand is of a different type, the resulting value is of the more general type
    - *Example: 2 `*` 2 is 4, whereas 2 `*` 2.0 is 4.0*

## Mixed-Mode Arithmetic and Type Casting

- **Mixed-Mode Arithmetic**
    - involves integers and floating point numbers
```shell
>>> 3.14 * 3 * 2
28.26
```
- You must a **type cast** when working with input of numbers
    - It is a function with the same name as the data type to which it converts
- Input function returns a string as its value
    - You can use the **int** or **float** cast to cast the string to a number before performing operations

| Type Cast                  | Example Use      | Value Returned |
|----------------------------|------------------|----------------|
| int(<a number or a string>) | int(3.77)        | 3              |
| int(<a number or a string>) | int('33')        | 33             |
| float(<a number or a string>)| float(22)       | 22.0           |
| str(<any value>)            | str(99)          | '99'           |

- Note that the **int** cast will cast a **float** to an **int** by truncation <ins>not</ins> by rounding
```shell
>>> int(6.75)
6
>>> round(6.75)
7
>>> round(6.75, 1)
6.8
```
- Type conversion also occurs in the construction of strings from numbers and other strings
```shell
>>> profit = 1000.55
>>> print('$' + profit)
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: cannot concatenate 'str' and 'float' objects
```
- Solution: use **str** cast
```shell
>>> print('$' + str(profit))
$1000.55
```
- Python is a **strongly typed** programming language

## Try-Except Statements

- **Try-Except Statement**
    - used to catch and handle exceptions
- Syntax:
```python
try:
    <statement>
except <exception type>:
    <statements>
finally:
    <statements>
```
- The **try** block allows you to test a block of code for errors
- The **except** block allows you to handle the error
- The **finally** block allows you to execute code regardless of the result of the previous blocks

## Example

```python
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try-except' is finished")
```

## Handling Multiple Exceptions

## Raising an Exception