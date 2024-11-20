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
    - JPEG (Joint Photographic Experts Group)
        - Uses **lossless compression** and a **lossy scheme**
    - GIF (Graphic Interchange Format)
        - Uses a lossy compression and a **color palette** of up to 256 of the most prevalent colors in the image

## Image-Manipulation Operations 

## The Properties of Images

## The `images` Module

## *A Loop Pattern for Traversing a Grid*

## A Word on Tuples 

## *Converting an Image to Black and White* 

## *Converting an Image to Grayscale*

## *Copying an Image*

## *Blurring an Image*

## *Edge Detection* 

## *Reducing the Image Size*
