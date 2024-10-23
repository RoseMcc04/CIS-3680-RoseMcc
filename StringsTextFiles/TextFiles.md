# Text Files

## Table of Contents

0. [Table of Contents](#table-of-contents)
1. [Objectives](#objectives)
2. [Motivation](#motivation)
3. [Text Files](#text-files)
    1. [Format of Text Files](#format-of-text-files)
4. [Writing Text to a File](#writing-text-to-a-file)
5. [Writing Numbers to a File](#writing-numbers-to-a-file)
6. [Reading Text from a File](#reading-text-from-a-file)
7. [Reading Numbers from a File](#reading-numbers-from-a-file)
8. [Summary of File Operations](#summary-of-file-operations)
9. [Accessing and Manipulating Files and Directories on Disk](#accessing-and-manipulating-files-and-directories-on-disk)

## Objectives

- Understand how to read text files
- Understand how to write text files
- Discuss file operations

## Motivation

- A place to save your strings
    - Long-term storage
    - Transport

## Text Files

- A text file is a software object that stores data on a permanent medium such as a disk or thumbdrive
- When compared to keyboard input from a human user, the main advantages of taking input data from a file are:
    - The dataset can be much larger
    - The data can accept input much quicker and with less chance of error
    - The data can be used repeatedly with the same program or different programs

### Format of Text Files

- Using a text editor such as *Notepad* or *TextEdit*, you can create, view, and save data in a text file
- A text file containing six floating-point numbers might look like:
```text
34.6 22.33 66.75
77.12 21.44 99.01
```
- All data output to or input from a text file must be <ins>strings</ins>
    - Number must be converted to string before output

## Writing Text to a File

- Data can be outputted to a text file using a **file** object
- To **open** a file for output:
```shell
>>> f = open("myfile.txt", 'w')
```
- If the file does not exist, <ins>it is created</ins>
- If it already exists, Python opens it; when data are written to the file and the file is closed, <ins>any data previously existing in the file are erased</ins>
- This statement writes two lines of text to the file:
```shell
>>> f.write("First line.\nSecond line.\n")
```
- When all outputs are finished, close the file:
```shell
>>> f.close()
```

## Writing Numbers to a File

- The **file** method **write** expects a string as an argument `f.write()`
    - Other types of data must first be converted to strings before being written to an output file (e.g., using **str()** or formatting)
- Code segment that illustrates the output of integers to a text file:
```python
import random
f = open("integers.txt", 'w')
for count in range(500):
    number = random.randint(1, 500)
    f.write(str(number) + '\n')
f.close()
```

## Reading Text from a File

- You open a file for input in a manner similar to opening a file for output
```shell
>>> f = open("myfile.txt", 'r')
```
    - If the path name is not accessible from the current working directory, Python raises an error
- There are several ways to read data from a file:
    - *Example: the **read()** method*
```shell
>>> text = f.read()
>>> text
'First line.\nSecond line.\n'
>>> print(text)
First line.
Second line.
```
- After input is finished, read() returns an empty string
- Files can look like a list of strings:
```python
f = open("myfile.txt", 'r')
for line in f:
    print(line)
```
```text
Output:

First line.
Second line.
```
- The readline method reads 1 line at a time:
```python
f = open("myfile.txt", 'r')
while True:
    line = f.readline()
    if line = " ":
        break
    print(line)
```
```text
Output: 

First line.
Second line.
```

## Reading Numbers from a File

- In Python, string representations of integers and floating-point numbers can be converted to the numbers by using the type casting of **`int()`** and **`float()`**
```python
f = open("integers.txt", 'r')
total = 0
for line in f:
    line = line.strip()
    number = int(line)
    total += number
print(f"The sum is {total}".)
```
- This code segment modifies the previous one to handle integers separated by spaces and/or new lines
```python
f = open("integers.txt", 'r')
total = 0
for line in f:
    word_list = line.split()
    for word in word_list:
        number = int(word)
        total += number
    print(f"The integer is: {number}".)
print(f"The sum is {total}.")
```

## Summary of File Operations

| Method          | What it Does                                                                 |
|-----------------|------------------------------------------------------------------------------|
| `open(filename, mode)` | Opens a file at the given filename and returns a file object. The mode can be 'r', 'w', 'tw', or 'a'. The last two values mean read/write and append. |
| `f.close()`     | Closes an output file. Not needed for input files.                           |
| `f.write(aString)` | Outputs `aString` to a file.                                              |
| `f.read()`      | Inputs the contents of a file and returns them as a single string. Returns "" if the end of the file is reached. |
| `f.readline()`  | Inputs a line of text and returns it as a string, including the newline. Returns "" if the end of the file is reached. |

## Accessing and Manipulating Files and Directories on Disk
