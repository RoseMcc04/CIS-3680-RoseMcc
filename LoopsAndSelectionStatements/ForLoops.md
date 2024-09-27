# For Loops

## Table of Contents
0. [Table of Contents](#table-of-contents)
1. [Prerequisites](#prerequisites)
2. [Execute a Statement a Finite Number of Times](#execute-a-statement-a-finite-number-of-times)
3. [Count-Controlled Loops](#count-controlled-loops)
4. [Loop Errors: Off-by-One Error](#loop-errors-off-by-one-error)
5. [Traversing the Contents of a Data Sequence](#traversing-the-contents-of-a-data-sequence)
6. [Specifying the Steps in the Range](#specifying-the-steps-in-the-range)
7. [Count Down Loops](#count-down-loops)
8. [Old-School Formatting Text for Output](#old-school-formatting-text-for-output)
9. [Newer Style Formatting Output](#newer-style-formatting-output)
10. [The f-string...](#the-f-string)

## Objectives

- Understand for-loops
- Discuss formatting output

## Prerequisites

- While loops
- Basic print function

## Execute a Statement a Finite Number of Times

- Python's for-loop is the control statement that most easily supports finite iteration
```shell
>>> for each_pass in range(4):
...    print("It's alive!", end = " ")
>>> It's alive! It's alive! It's alive!
```
- The form of this type of loop is:
```text
for <variable> in range(<an integer expression>):
    <statement-1>

    <statement-n>
```
- First line of code is sometimes called the loop header
- The rest of the code is the loop body (must be indented and aligned in the same column)
- *Example: Loop to compute an exponentiation for a non-negative exponent*
```shell
>>> number = 2
>>> exponent = 3
>>> product = 1
>>> for each_pass in range(exponent):
        product *= number
        print(product, end = " ")
2 4 8
>>> product
8
```
- If the exponent were 0, the loop body would not execute and the value of the product would remain as 1

## Count-Controlled Loops

- Loops that count through a range of numbers
```shell
>>> product = 1
>>> for count in range(4):
        product *= count + 1
>>> product
24
```
- To specify an explicit lower bound:
```shell
>>> product = 1
>>> for count in range(1, 5):
        product *= count
>>> product
24
```
- *Example: bound-delimited summation*
```python
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
total = 0
for number in range(lower, upper + 1):
    total += number
print(total)
```
```text
Output 
Enter the lower bound: 1
Enter the upper bound: 10
55
```

## Loop Errors: Off-by-One Error

- *Example*
```shell
>>> # Count from 1 through 4, we think
>>> for count in range(1, 4):
        print(count)
1
2
3
```
- Loop actually counts from 1 through 3
- Not a syntax error, but rather a logic error

## Traversing the Contents of a Data Sequence

- **range()**
    - basically returns a **list**
```shell
>>> list(range(4))
[0, 1, 2, 3]
>>> list(range(1, 5))
[1, 2, 3, 4]
```
- Strings are also sequences of characters
- Values in a sequence can be visited with a for-loop:
```text
for <variable> in <sequence>:
    <do something with the variable>
```
- *Example*
```shell
>>> for char in "Hi there!":
        print(char, end = " ")
H i  t h e r e !
```

## Specifying the Steps in the Range

- **range()** allows a third argument that allows you to specify a **step value**
```shell
>>> list(range(1, 6, 1))
[1, 2, 3, 4, 5]
>>> list(range(1, 6, 2))
[1, 3, 5]
>>> list(range(1, 6, 3))
[1, 4]
```
- *Example*
```shell
>>> theSum = 0
>>> for count in range(2, 11, 2):
        theSum += count
>>> theSum
30
```

## Count Down Loops

- *Example*
```shell
>>> for count in range(10, 0, -1):
        print(count, end = " ")
    10 9 8 7 6 5 4 3 2 1 
>>> list(range(10, 0, -1)):
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

## Old-School Formatting Text for Output

- Many data-processing applications require output that has **tabular format**
- **Field width**
    - Total number of data characters and additional spaces for a datum in a formatted string
- The **print()** function automatically begins printing an output datum in the first available column
```shell
>>> for exponent in range(7, 11):
...     print(exponent, 10 ** exponent)
7 10000000
8 100000000
9 1000000000
10 10000000000
```
- <**format string**> % <**datum**>
- This version contains a **format string, format operator %**, and single data value to be formatted
    = To format integers, letter **d** is used instead of **s**
- To format sequence of data values:
    - <format string> % (<datum-1>, ..., <datum-n>)
```shell
>>> for exponent in range(7, 11):
...     print("%03d%12d" % (exponent, 10 ** exponent))
7   10000000
8   100000000
9   1000000000
10  10000000000
```
- To format data value of type float:
    %<field width>.<precision>f where .<precision> is optional
- *Examples*
```shell
>>> salary = 100.00
>>> print("Your salary is $" + str(salary))
Your salary is $100.0
>>> print("Your salary is $%0.2f" % salary)
Your salary is $100.00
```

## Newer Style Formatting Output

```python
msg = "x: {} y: {1:10.3f}".format(x, y)
print(msg)
```
- A string serves as a template with replacement fields; The format method prepares the data according to the format specification and plugs it into the template for printing
- Replacement fields take the form:
    - {variable_index[:FormatSpec]}
- Format specifications:
    - [[fill]align][sign][#][0][width][grouping_option][.precision][type]

| Type | Meaning |
|------|---------|
| None | The same as `g`. |
| `f`  | Decimal integer. Outputs the number in base 10. |
| `e`  | Exponent notation. Prints the number in scientific notation using the letter `e` to indicate the exponent. The default precision is 6. |
| `E`  | Exponent notation. Same as `e` except it uses an uppercase letter `E` as the exponent character. |
| `F`  | Fixed-point notation. Displays the number as a fixed-point number. The default precision is 6. |
| `g`  | Fixed-point notation, same as `f`, but converts a ratio to NAN and INF to INF. |
| `%`  | Percentage. Multiplies the number by 100 and displays it in fixed `f` format, followed by a percent sign. |
| `b`  | Binary format. Outputs the number in base 2. |
| `c`  | Character. Converts the integer to the corresponding unicode character before printing. |
| `o`  | Octal format. Outputs the number in base 8. |
| `x`  | Hex format. Outputs the number in base 16, using lower-case letters for the digits above 9. |
| `X`  | Hex format. Outputs the number in base 16, using upper-case letters for the digits above 9. |
| `n`  | Number. This is the same as `g`, except that it uses the current locale setting to insert the appropriate number separator characters. |

| Align | Meaning |
|-------|---------|
| `<`   | Field to be left-aligned within the available space (this is the default for most objects). |
| `>`   | Field to be right-aligned within the available space (this is the default for numbers). |
| `=`   | Forces the padding to be placed after the sign (if any) but before the digits. This is used for printing fields in the form `+000000120`. This alignment option is valid only for numeric types. It becomes the default when '0' immediately precedes the field width. |
| `^`   | Field to be centered within the available space. |

## The f-string...

- The last, and probably easiest, way to do formatting
- Like newer style, but without the variable numbering, just use the variable name in the place holder
```python
msg = "x: {x:5.2f} y: {y:10.3f}"
print(msg)
```