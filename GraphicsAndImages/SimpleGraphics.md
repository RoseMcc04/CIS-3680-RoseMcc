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
![Turtle Graphics Window](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTN3yOXOnguRZ_CDOPNSuiwuFW4uUM_L1xdHg&s) <br>
- To close a turtle's window, click its close box
- Attempting to manipulate a turtle whose window has been closed raises an error

## Draw Two-Dimensional Shapes

- The code for a function to draw a pattern called `radialHexagons()`, expects a turtle, the number of hexagons, and the length of a side as arguments:
```python
def radialHexagons(t, n, length):
    """ Draws a radial pattern of n hexagons with the given length. """
    for count in range(n):
        hexagon(t, length)
        t.left(360 / n)
```

- The code for drawing a radial pattern using any regular polygon followed by a session using it for squares and hexagons:
```python
def radialpattern(t, n, length, shape):
    """ Draws a radial pattern of n shapes with the given length. """
    for count in range(n):
        shape(t, length)
        t.left(360 / n)
```
```shell
>>> t = Turtle()
>>> radialPattern(t, n = 10, length = 50, shape = square)
>>> t.clear()
>>> radialPattern(t, n = 10, length = 50, shape = hexagon)
```

## Examining an Object's Attributes

- **Mutator methods**
    - methods that change the internal state of a Turtle object
- **Accessor methods**
    - methods that return the values of a Turtle object's attributes without altering its state
- Code that shows accessor methods in action:
```shell
>>> from turtle import Turtle
>>> t = Turtle()
>>> t.position()
(0.0, 0.0)
>>> t.heading()
0.0
>>> t.isdown()
True
```

## Manipulating a Turtle's Screen

- Access a turtle's **Screen** object bu using the prompt **t.screen**
    - Then call a Screen method with this object
- Methods **window_width()** and **window_height()** can be used to locate the boundaries of a turtle's window
- Code that resets the screen's background color:
```python
from turtle import Turtle
t = Turtle()
t.screen.bgcolor("orange")
x = t.screen.window_width() // 2
y = t.screen.window_height() // 2
print((-x, y), (x, -y))
```

## Taking a Random Walk

```python
from turtle import Turtle
import random

def randomWalk(t, turns, distance = 20):
    """ Turns a random number of degrees and moves a given distance for a fixed number of turns. """
    for x in range(turns):
        if x % 2 == 0:
            t.left(random.randInt(0, 270))
        else:
            t.right(random.randInt(0, 270))
        t.forward(distance)

def main():
    t = Turtle()
    t.shape("turtle")
    randomWalk(t, 40, 30)

if __name__ == "__main__":
    main()
```

## Colors and the RGB System

- Display area on a computer screen is made up of colored dots called picture elements or **pixels**
- Each pixel represents a color - default is black
    - Change the color by running the **pencolor()** method
- RGB is a common system for representing colors
    - RGB stands for red, green, and blue
    - Each color component can range from 0-255
        - 255 --> macimum saturation of a color component
        - 0 --> total absence of that color component
    - A **true color** system
- Each color component requires 8 bits; total number of bits needed to represent a color value is 24
