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

## Mixed-Mode Arithmetic and Type Casting

## Try-Except Statements

## Example

## Handling Multiple Exceptions

## Raising an Exception