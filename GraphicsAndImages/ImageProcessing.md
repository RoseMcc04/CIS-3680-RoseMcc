# Image Processing 

## Table of Contents 

0. [Table of Contents](#table-of-contents)
1. [Objectives](#objectives)
2. [Image Processing](#image-processing-1)
3. [Analog and Digital Information](#analog-and-digital-information)
4. [Sampling and Digitizing Images](#sampling-and-digitizing-images)
5. [Image File Formats](#image-file-formats)
6. [Image-Manipulation Operations](#image-manipulation-operations)
7. [The Properties of Images](#the-properties-of-images)
8. [The `images` Module](#the-images-module)
9. [*A Loop Pattern for Traversing a Grid*](#a-loop-pattern-for-traversing-a-grid)
10. [A Word on Tuples](#a-word-on-tuples)
11. [*Converting an Image to Black and White*](#converting-an-image-to-black-and-white)
12. [*Converting an Image to Grayscale*](#converting-an-image-to-grayscale)
13. [*Copying an Image*](#copying-an-image)
14. [*Blurring an Image*](#blurring-an-image)
15. [*Edge Detection*](#edge-detection)
16. [*Reducing the Image Size*](#reducing-the-image-size)

## Objectives 

- Develop recursive algorithms to draw recursive shapes
- Write a nested loop to process a two-dimensional grid
- Develop algorithms to perform simple transformations of images, such as conversion of color to grayscale

## Image Processing 

- Digital image processing includes the principles and techniques for the following:
    - The capture of images with devices such as flatbed scanners and digital cameras 
    - The representation and storage of images in efficient file formats 
    - Constructing the algorithms in image-manipulation programs such as *Adobe Photoshop*

## Analog and Digital Information 

- Computers must use digital information which consists of **discrete values**
    - *Examples: Individual integers, characters of text, or bits*
- The information contained in images, sound, and much of the rest of the world is analog 
    - **Analog information** contains a **continuous range** of values 
- Ticks representing seconds on an analog clock's face represent an attempt to **sample** moments of time as discrete values (time itself is continuous)

## Sampling and Digitizing Images 

- A visual scene projects an infinite set of color and intensity values onto a two-dimensional sensing medium
    - If you sample enough of these values, digital information can represent an image more or less distinguishable (to the human eye) from the origin scene
- Sampling devices measure discrete color values at distinct points on a two-dimension **grid**
    - These values are pixels
    - As more pixels are sampled, the more realistic the resulting image will appear

## Image File Formats

- Once an image has been sampled, it can be stored in one of many file formats
- A **raw image file** saves all the sampled information 
- Data can be compressed to minimize its file size
    - *JPEG (Joint Photographic Experts Group)*
        - Uses **lossless compression** and a **lossy scheme**
    - *GIF (Graphic Interchange Format)*
        - Uses a lossy compression and a **color palette** of up to 256 of the most prevalent colors in the image

## Image-Manipulation Operations 

- Image-manipulation programs either transform the information in the pixels or alter the arrangement of the pixels in the image
- *Examples:*
    - *Rotate an image*
    - *Convert an image from color to grayscale*
    - *Apply color filtering to an image*
    - *Highlight a particular area in an image*
    - *Blur all or part of an image*
    - *Sharpen all or part of an image*
    - *Control the brightness of an image*
    - *Perform edge detection on an image*
    - *Enlarge or reduce an image's size*
    - *Apply color inversion to an image*
    - *Morph an image into another image*

## The Properties of Images

- The coordinates of pixels in the two-dimensional grid of an image range from (0, 0) at the upper-left corner to **(width - 1, height - 1)** at the lower-right corner
    - **width/height** are the image's dimension in pixels
    - Thus, the **screen coordinate system** for the display of an image is different from the standard Cartesian coordinate system we used with Turtle graphics
- The RGB color system is a common way of representing the colors in images

## The `images` Module

- The images module is a non-standard, open-source Python tool
    - Image class represents an image as a two-dimensional grid of RGB values
- The following session with the interpreter does the following:
    - Imports the Image class from the images module
    - Instantiates this class using the file named `smokey.gif`
    - Draws the image
```shell
>>> from images import Image
>>> image = Image("smokey.gif")
>>> image.draw()
```
- Once an image has been created, you can examine its width and height as follows:
```shell
>>> image.getWidth()
198
>>> image.getHeight()
149
```
- Alternatively, you can print the image's string representation:
```shell
>>> print(image)
Filename: smokey.gif
Width: 198
Height: 149
```
- The method **getPixel(x, y)** returns a tuple of the RGB values at the given coordinates
- The following session shows the information for the pixel at position (0, 0):
```shell
>>> image.getPixel(0, 0)
(194, 221, 114)
```
- You can use the method **setPixel(x, y, color)** to replace a RGB value at a given position in the image:
```shell
>>> image = Image(150, 150)
>>> image.draw()
>>> blue = (0, 0, 255)
>>> y = image.getHeight() // 2
>>> for x in range(image.getWidth())
        image.setPixel(x, y - 1, blue)
        image.setPixel(x, y, blue)
        image.setPixel(x, y + 1, blue)
>>> image.draw()
```
- Use the save operation to write an image back to an existing file using the current filename
- The following code saves the new image using the filename `horizontal.gif`:
```shell
>>> image.save("horizontal.gif")
```

## *A Loop Pattern for Traversing a Grid*

## A Word on Tuples 

- A pixel's RGB values are stored in a tuple:
```shell
>>> image = Image("smokey.gif")
>>> (r, g, b) = image.getPixel(0, 0)
>>> r
194
>>> g
221
>>> b
114
>>> image.setPixel(0, 0, (r + 10, g + 10, b + 10))
```

## *Converting an Image to Black and White* 

## *Converting an Image to Grayscale*

## *Copying an Image*

## *Blurring an Image*

## *Edge Detection* 

## *Reducing the Image Size*
