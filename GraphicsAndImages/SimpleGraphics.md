# Simple Graphics

## Table of Contents

0. [Table of Contents](#table-of-contents)
1. [Objectives](#objectives)
2. [Simple Graphics](#simple-graphics-1)
3. [Overview of Turtle Graphics](#overview-of-turtle-graphics)
4. [Turtle Operations](#turtle-operations)
5. [Setting Up a `turtle.cfg` File](#setting-up-a-turtlecfg-file)
6. [Object Instantiation and the Turtle Module](#object-instantiation-and-the-turtle-module)
7. [Draw Two-Dimensional Shapes](#draw-two-dimensional-shapes)
8. [Examining an Object's Attributes](#examining-an-objects-attributes)
9. [Manipulating a Turtle's Screen](#manipulating-a-turtles-screen)
10. [Taking a Random Talk](#taking-a-random-walk)
11. [Colors and the RGB System](#colors-and-the-rgb-system)

## Objectives

- Use the concepts of object-oriented programming - classes, objects, and methods - to solve a problem
- Develop algorithms that use simple graphics operations to draw two-dimensional shapes
- Use the RGB system to create colors in graphics applications and modify pixels in images

## Simple Graphics

- **Graphics**
    - Discipline that underlies the representation and display of geometric shapes in two-and-three-dimensional space
- **Turtle graphics**
    - Toolkit that provides a simple and enjoyable way to draw pictures in a window
    - **turtle** is a non-standard, open-source Python module

## Overview of Turtle Graphics

- Turtle graphics originally developed as part of the children's programming language, **Logo**
    - *Created by Seymour Papert and his colleagues at MIT in the late 1960s*
- Analogy: Turtle crawling on a piece of paper, with a pen tied to its tail
    - Sheet of paper is a window on a display screen
    - Position specified with **(x, y)** coordinates
        - Cartesian **coordinate system**, with origin (0, 0) at the center of the window

| Turtle Attribute | Description |
|------------------|-------------|
| Heading          | Specified in degrees, the heading or direction increases in value as the turtle turns to the left, or counterclockwise. Conversely, a negative quantity of degrees indicates a right, or clockwise, turn. The turtle is initially facing east, or 0 degrees. North is 90 degrees. |
| Color            | Initially black, the color can be changed to any of more than 16 million other colors. |
| Width            | This is the width of the line drawn when the turtle moves. The initial width is 1 pixel. (You'll learn more about pixels shortly.) |
| Down             | This attribute, which can be either true or false, controls whether the turtle's pen is up or down. When true (that is, when the pen is down), the turtle draws a line when it moves. When false (that is, when the pen is up), the turtle can move without drawing a line. |

## Turtle Operations

| Turtle Method                        | What It Does                                                                                  |
|--------------------------------------|-----------------------------------------------------------------------------------------------|
| `t = Turtle()`                       | Creates a new `Turtle` object and opens its window                                            |
| `t.home()`                           | Moves `t` to the center of the window and then points `t` east                                |
| `t.up()`                             | Raises `t`'s pen from the drawing surface                                                     |
| `t.down()`                           | Lowers `t`'s pen to the drawing surface                                                       |
| `t.setheading(degrees)`              | Points `t` in the indicated direction, which is specified in degrees                          |
| `t.left(degrees)` / `t.right(degrees)` | Rotates `t` to the left or the right by the specified degrees                                |
| `t.goto(x, y)`                       | Moves `t` to the specified position                                                           |
| `t.forward(distance)`                | Moves `t` to the specified distance in the current direction                                  |
| `t.pencolor(r, g, b)` / `t.pencolor(string)` | Changes the pen color of `t` to the specified RGB value or to the specified string         |
| `t.fillcolor(r, g, b)` / `t.fillcolor(string)` | Changes the fill color of `t` to the specified RGB value or to the specified string      |
| `t.begin_fill()` / `t.end_fill()`    | Encloses a set of turtle commands that will draw a filled shape using the current fill color   |
| `t.clear()`                          | Erases all of the turtle's drawings, without changing the turtle's state                      |
| `t.width(pixels)`                    | Changes the width of `t` to the specified number of pixels                                    |
| `t.hideturtle()` / `t.showturtle()`  | Makes the turtle invisible or visible                                                         |
| `t.position()`                       | Returns the current position `(x, y)` of `t`                                                 |
| `t.heading()`                        | Returns the current direction of `t`                                                         |
| `t.isdown()`                         | Returns `True` if `t`'s pen is down or `False` otherwise                                      |

- **Interface**
    - a set of methods of a given class
        - Used to interact with an object
        - Use docstring mechanism to view an interface
        - **help(classname)**
        - **help(classname.methodname())**
```python
def drawSquare(t, x, y, length):
    """ Draws a square with the given turtle t, an upper-left corner point (x, y), and a side's length. """
    t.up()
    t.goto(x, y)
    t.setheading(270)
    t.down()
    for count in range(4):
        t.forward(length)
        t.left(90)
```

## Setting Up a `turtle.cfg` File

- Turtle graphics configuration file (turtle.cfg)
    - Contains initial settings of several attributes of **Turtle**, **Screen**, and **Canvas** objects
    - Python creates default settings for these attributes
- The attributes in the file used for most of our examples are:
    - `width` = 300
    - `height` = 200
    - `colormode` = 255
    - `using_IDLE` = True
- To create a file with these settings:
    - Open a text editor, enter the settings, and save the file as turtle.cfg

## Object Instantiation and the Turtle Module

- Before you apply any methods to an object, you must create the object (i.e., an **instance** of)
- **Instantiation**
    - Process of creating an object
- Use a **constructor** to instantiate an object:
```text
<variable name> = <class name>(<any arguments>)
```
- To instantiate the **Turtle** class:
```shell
>>> from turtle import Turtle
>>> t = Turtle()
```
![Turtle Graphics Window](data:image/png;base64,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) <br>
- To close a turtle's window, click its close box
- Attempting to manipulate a turtle whose window has been closed raises an error

## Draw Two-Dimensional Shapes

## Examining an Object's Attributes

## Manipulating a Turtle's Screen

## Taking a Random Walk

## Colors and the RGB System
