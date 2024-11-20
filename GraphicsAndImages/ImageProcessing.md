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

- The following loop uses a row-major traversal
```shell
>>> width = 2
>>> height = 3
>>> for y in range(height):
    for x in range(width):
        print((x, y), end = " ")
        print()
(0, 0) (1, 0)
(0, 1) (1, 1)
(0, 2) (1, 2)
```
- We use this templateto develop many of the algorithms that follow: 
```text
for x in range(width):
    for y in range(height):
        <do something at position (x, y)>
```

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

- For each pixel, compute an average of RGB values
- Then, reset pixel's color values to 0 (black) if the average is closer to 0, or in 255 (white) if the average is closer to 255
```python
def blackAndWhite(image):
	“““Converts the argument image to black and white.”””
	blackPixel = (0, 0, 0)
	whitePixel = (255, 255, 255)
	for y in range(image.getHeight()):
	   for x in range(image.getWidth()):
		(r, g, b) = image.getPixel(x, y)
		average = (r + g + b) // 3
		if average < 128:
		   image.setPixel(x, y, blackPixel)
		else:
		   image.setPixel(x, y, whitePixel)
```

## *Converting an Image to Grayscale*

- Black and white photographs contain various shades of gray known as grayscale
- Grayscale can be an economical scheme (only color values might be 8, 16, or 256 shades of gray)
- A simple method:
```python
average = (r + g + b) // 3
image.setPixel(x, y, (average, average, average))
```
- Problem: Does not reflect manner in which different color components affect human perception
- Scheme needs to take differences in luminance into account
```python
def grayscale(image):
	“““Converts the argument image to grayscale.”””
	for y in range(image.getHeight()):
	   for x in range(image.getWidth()):
	   (r, g, b) = image.getPixel(x, y)
	   r = int(r * 0.299)
	   g = int(g * 0.587)
	   b = int(b * 0.114)
	   lum = r + g + b
	   image.setPixel(x, y, (lum, lum, lum))
```

## *Copying an Image*

- The method **clone()** builds and returns a new image with the same attributes as the original one, but with an empty string as the filename
```python
>>> from images import Image
>>> image = Image("smokey.gif")
>>> image.draw()
>>> newImage = image.clone() # Create a copy of image
>>> newImage.draw()
>>> grayscale(newImage) # Change in second window only
>>> newImage.draw()
>>> image.draw() # Verify no change to original
```

## *Blurring an Image*

- Pixelation can be mitigated by blurring:
```python
def blur(image):
    """Builds and returns a new image which is a
    blurred copy of the argument image."""
    def tripleSum(triple1, triple2):
	   (r1, g1, b1) = triple1
	   (r2, g2, b2) = triple2
	   return (r1 + r2, g1 + g2, b1 + b2)
    new = image.clone()
    for y in range(1, image.getHeight() - 1):
    for x in range(1, image.getWidth() - 1):
        old P = image.getPixel(x, y)
	   left = image.getPixel(x - 1, y) # To left
	   right = image.getPixel(x + 1, y) # To right
	   top = image.getPixel(x, y - 1) # Above
	   bottom = image.getPixel(x, y + 1) # Below
	   sums = reduce(tripleSum, [oldP, left, right, top, bottom])
	   averages = tuple(map(lambda x: x // 5, sums))
	   new.setPixel(x, y, averages)
    return new
```

## *Edge Detection* 

- Edge detection removes the full colors to uncover the outlines of the objects represented in the image
```python
def detectEdges(image, amount):
	“““Builds and returns a new image in which the edges of
	the argument image are highlighted and the colors are
	reduced to black and white.”””

	def average(triple):
	    (r, g, b) = triple
	    return (r + g + b) // 3

	blackPixel = (0, 0, 0)
	whitePixel = (255, 255, 255)
	new = image.clone()
    for y in range(image.getHeight() − 1):
	for x in range(1, image.getWidth()):
	   oldPixel = image.getPixel(x, y)
	   leftPixel = image.getPixel(x − 1, y)
	   bottomPixel = image.getPixel(x, y + 1)
	   old Lum = average(oldPixel)
	   left Lum = average(leftPixel)
	   bottom Lum = average(bottomPixel)
	   if abs(oldLum − leftLum) > amount or \
		abs(oldLum − bottomLum) > amount:
		new.setPixel(x, y, blackPixel)
	   else:
		new.setPixel(x, y, whitePixel)
    return new
```

## *Reducing the Image Size*

- The size and quality of an image on a display medium depend on two factors:
    - Image's width and height in pixels
    - Display medium's **resolution**
        - Measured in pixels, or dots per inch
- The resolution of an image can be set before the image is captured
    - A higher dots per inch causes sampling device to take more samples (pixels) through the two-dimensional grid
- A size reduction usually preserves an image's **aspect ratio**
- Reducing an image's size throws away some of its pixel information
```python
def shrink(image, factor):
	“““Builds and returns a new image which is a smaller
	copy of the argument image, by the factor argument.”””
	width = image.getWidth()
	height = image.getHeight()
	new = Image(width // factor, height // factor)
	oldY = 0
	newY = 0
	while oldY < height - factor:
	   oldX = 0
	   newX = 0
	   while oldX < width - factor:
		oldP = image.getPixel(oldX, oldY)
		new.setPixel(newX, newY, oldP)
		oldX += factor
		newX += 1
	   oldY += factor
	   newY += 1
	return new
```
