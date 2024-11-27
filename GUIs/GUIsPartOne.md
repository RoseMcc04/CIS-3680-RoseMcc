# Graphical User Interfaces (GUIs) Part 1

## Table of Contents

0. [Table of Contents](#table-of-contents)
1. [Objectives](#objectives)
2. [Introduction](#introduction)
3. [Terminal-Based Programs vs. GUI-Based Programs](#terminal-based-programs-vs-gui-based-programs)
    1. [*Terminal-Based Example*](#terminal-based-example)
    2. [*GUI-Based Example*](#gui-based-example)
4. [Event-Driven Programming](#event-driven-programming)
5. [Coding Simple GUI-Based Programs](#coding-simple-gui-based-programs)
6. [*Example: A Simple "Hello world!" Program*](#example-a-simple-hello-world-program)
7. [A Template for All GUI Programs](#a-template-for-all-gui-programs)
8. [Syntax of Class and Method Definitions](#syntax-of-class-and-method-definitions)
9. [Subclassing and Inheritance as an Abstraction Mechanism](#subclassing-and-inheritance-as-abstraction-mechanisms)
10. [Windows and Window Components](#windows-and-window-components)
11. [Windows and Their Attributes](#windows-and-their-attributes)
12. [Window Layout](#window-layout)
13. [Types of Window Components and Their Attributes](#types-of-window-components-and-their-attributes)
14. [Displaying Images](#displaying-images)
15. [Command Buttons and Responding to Events](#command-buttons-and-responding-to-events)
16. [Input and Output with Entry Fields](#input-and-output-with-entry-fields)
17. [Text Fields](#text-fields)

## Objectives

- Design and code a GUI-based program 
- Define a new class using subclassing and inheritance 
- Instantiate and lay out different types of window objects, such as labels, entry fields, and command buttons in a window's frame 
- Define methods that handle events associated with window objects

## Introduction

- Most modern computer software employs a **graphical user intergface (GUI)**
- A GUI displays text as well as small images (called icons) that represent objects such as directories, files of different types, command buttons, and drop-down menus 
- In addition to entering text at a keyboard, the user of a GUI can select an icon with a pointing device, such as a mouse, and move that icon around on the display 

## Terminal-Based Programs vs. GUI-Based Programs

- Two different versions of the same program from a user's perspective:
    - Terminal-based interface 
    - Graphical user interface 
- Both programs perform exactly the same function 
    - However, their behavior, or look and feel, from a user's perspective are quite different 

### *Terminal-Based Example*

- Terminal-based user interface has several effects on its users: 
    - User is constrained to a definite sequence of prompts for inputs 
        - Once an input is entered, there is no way of changing it  
    - To obtain results for a different set of input data, the user must wait forf the command menu to be displayed again 
        - At that point, the same command and all of the other inputs must be re-entered 
![Terminal User I/O Image](https://marketing.invisionapp-cdn.com/cms/images/lr1orcar/marketing-pages/045a753ba335852a1d1f4b1dac503787532b0b0f-1440x1080.png?w=2000&fm=jpg&q=90)

### *GUI-Based Example*

- GUI-based version displays a window that contains various components 
    - Called **window objects** or **widgets**
- GUI-based version has the following effects on users:
    - User is not constrained to enter inputs in a particular order  
        - Before pressing the Compute button, the user an edit any of the data 
    - Running different data sets does not require re-entering all of the data 
- GUIs seem to be a definite improvement over the terminal-based user interfaces 
![GUI User I/O Image](https://new.pythonforengineers.com/content/images/2021/08/pyqt_top-1.jpg)

## Event-Driven Programming

- User-generated **events** (e.g., mouse clicks) trigger operations in the program to respond by pulling in inputs, processing them, and displaying results 
    - **Event-driven** software 
    - **Event-driven programming**
- Coding phase:
    - Define a new class to represent the main window 
    - Instantiate the classes of window objects needed for this application (e.g., labels, command buttons) 
    - Position these components in the window 
    - Instantiate the data model and provide any default data in the window objects 
    - Register controller methods with each window object in which a relevant event might occur 
    - Define these controller methods 
    - Define a **main()** that launches the GUI 

## Coding Simple GUI-Based Programs

- There are many libraries and toolkits of GUI components available to the average Python programmer 
    - **tkinter** includes classes for windows and numerous types of window objects 
    - **breezypythongui** is a custom, open-source module for GUI development 

## *Example: A Simple "Hello world!" Program*

- A new window class extends the EasyFrame class 
- The EasyFrame class provides the basic functionality for any window 
```python
"""
File: labeldemo.py
"""
from breezypythongui import Easy Frame
class LabelDemo(EasyFrame):
    """
    Displays a greeting in a window.
    """
    def __init__(self):
        """
        Sets up the window and the label.
        """
        EasyFrame.__init__(self)
        self.addLabel(text = "Hello world!", row = 0, column = 0)

def main():
    """
    Instantiates and pops up the window.
    """
    LabelDemo.mainloop()

if __name__ == "__main__":
    main()
```

## A Template for All GUI Programs

- The structure of a GUI program is always the same, so there is a template: 
```text
from breezypythongui import EasyFrame 

class ApplicationName(EasyFrame):
    __init__(self):
        # Definitions of event handling methods

def main():
    ApplicationName().mainloop()

if __name__ == "__main__":
    main()
```

## Syntax of Class and Method Definitions

- Each definition has a one-line header that begins with a keyword (class or def) 
    - Followed by a body of code indented one level in the text 
- A class header contains the name of the class followed by a parenthesized list of one or more parent classes 
- The body, nested one tab under the header, consists of one or more method definitions 
- A method header looks like a function header 
    - But a method always has at least one parameter named **self**

## Subclassing and Inheritance as Abstraction Mechanisms

![Inheritance Example Diagram](https://www.cs.colostate.edu/~cs163/.Summer20/assets/img/labs/UML_Lab_16.png)

## Windows and Window Components

- This section explores the details of windows and window components
- You will also learn how to:
    - Choose appropriate classes of GUI objects 
    - Access and modify their attributes 
    - Organize them to cooperate to perform the task at hand 

## Windows and Their Attributes

- Most important attributes: 
    - Title (an empty string by default) 
    - Width and height in pixels 
    - Resizability (true by default) 
    - Background color (white by default)
- *Example of overriding dimensions and title:*
```python
EasyFrame.__init__(self, width = 300, height = 200, title = "Label Demo")
```
| EasyFrame Method      | What It Does                                           |
|-----------------------|-------------------------------------------------------|
| setBackground(color)  | Sets the window's background color to `color`         |
| setResizable(boolean) | Makes the window resizable (`True`) or not (`False`)  |
| setSize(width, height)| Sets the window's width and height in pixels          |
| setTitle(title)       | Sets the window's title to `title`                    |

## Window Layout

- Window components are laid out in the window's two-dimensional **grid** 
    - Rows and columns are numbered from the position (0, 0) in the upper left corner of the window 
- *Example:*
```python
from breezypythongui import EasyFrame

class LayoutDemo(EasyFrame):
    """
    Displays labels in the quadrants.
    """
    def __init__(self):
        """
        Sets up the window and the labels.
        """
        EasyFrame.__init__(self)
        self.addLabel(text = "(0, 0)", row = 0, column = 0)
        self.addLabel(text = "(0, 1)", row = 0, column = 1)
        self.addLabel(text = "(1, 0)", row = 1, column = 0)
        self.addLabel(text = "(1, 1)", row = 1, column = 1)
```
- Each type of window component has a default alignment 
- Programmers can override the default alignment by including the **sticky** attribute as a keyword argument 
```python
self.addLabel(text = "(0, 0)", row = 0, column = 0, sticky = "NSEW")
self.addLabel(text = "(0, 1)", row = 0, column = 1, sticky = "NSEW")
self.addLabel(text = "(1, 0)", row = 1, column = 0, sticky = "NSEW")
self.addLabel(text = "(1, 1)", row = 1, column = 1, sticky = "NSEW")
```

## Types of Window Components and Their Attributes

## Displaying Images

## Command Buttons and Responding to Events

## Input and Output with Entry Fields

## Text Fields
