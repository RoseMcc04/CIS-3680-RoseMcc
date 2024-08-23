# Business Computing

## Table of Contents
1. [Why programming?](#why-programming)
2. [Objectives](#objectives)
3. [Venn Diagram](#venn-diagram)
4. [An Information System](#an-information-system)
5. [Building an Information System](#building-an-information-system)
6. [Algorithms](#algorithms)
7. [Information Processing](#information-processing)
8. [Modern Computer Structure](#modern-computer-structure)
9. [Computer Hardware](#computer-hardware)
10. [System Bus](#system-bus)
11. [Computer Software](#computer-software)
12. [How Computer Software is Made](#how-computer-software-is-made)

## Why programming?

- Analytics defined (Oxford)
    - The systematic computational analysis of data or statistics
    - Information resulting from the systematic analysis of data or statistics
- Computers are the only way to handle all the data
- Off-the-shelf software can be limiting

## Objectives

1. Define what is meant by an information system
2. Define and describe algorithms
3. Describe information processing
4. Examine the structure of an information system
5. Describe how an application is made

## Venn Diagram
```css
+-------------------+       +-------------------+
|                   |       |                   |
|                   |       |                   |
|     Business      |       |    Technology     |
|                   |       |                   |
|                   |       |                   |
+-------------------+       +-------------------+
            \                   /
             \                 /
              \               /
                +-------------+
                | Information |
                |  Systems    |
                +-------------+

```

## An Information System

- A set of interrelated components that collect, process, store, and distribute information to support decision making and control in an organization
- This includes analysis and visualization
- Analytics applications are a subset of Information Systems Applications

## Building an Information System

- We will focus on a broad set of interrelated ideas
- Two fundamental ideas are algorithms and information processing

## Algorithms

- A process or set of rules to be followed in calculations or other problem-solving operations, especially by a computer
- Features of an algorithm:
    - Consists of a finite number of instructions
    - Each individual instruction is well defined
        - Action described by the instruction can be performed effectivelty or be executed by a computing agent
    - Eventually stops after arriving at a solution to a problem
    - Solves a general class of problems
- Examples: Baking a cake, Changing a tire, Math operations

## Information Processing

- Information is commonly referred to as data
- In carrying out the instructions of an algorithm, the computing agent manipulates information
    - Input data
    - Process (transform) information according to well-defined rules
    - Computer scientists have discovered ways to represent many other things, such as images, sound, and video

## Modern Computer Structure

- Hardware:
    - physical devices required to execute algorithms
- Software:
    - set of these algorithms, represented as programs in particular programming languages

## Computer Hardware

- Basic hardware components of a computer are:
    - Central processing unit (CPU)
    - Memory
    - Set of I/O devices
- Computers can also communicate with the external world through various ports that connect them to networks and to other devices

| Part of CPU | Description |
|-------------|-------------|
| Control Unit| Instructions|
|  Logic Unit |Math/Decision|
| Cache Memory| Buffer/Data |
|  Registers  |Work. Memory |

## System Bus
- Processor
    - CPU <-- ROM --> Connection Unit
- Main Memory
- Disk
- Screen
- Keyboard
- Network
- Other Peripherals

## Computer Software

- The most important part of system software is a computer's operating system
    - Some important parts: file system, user-interfaces (terminal-based, GUIs, or touchscreen interfaces)
- Applications include web browsers, word processors, spreadsheets, database managers, graphic design packages, CRMs, etc. 
- A program stored in computer memory must be represented in binary digits, or machine code
- A loader takes a set of machine language instructions as input and loads them into the appropriate memory locations

## How Computer Software is Made

- Scientists have developed high-level programming languages for expressing algorithms that resemble English
- Programmers usually start by writing high-level language statements, called source code, in a text editor
- Another program called a compiler or interpreter converts program code into executable code
- If no errors are found, the program can be executed by the runtime system
    - Might execute program directly on the hardware or run another program called a virtual machine to execute the program 
