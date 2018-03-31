#!/usr/bin/env python
"""
This script uses OpenCV for Python 3.
It fills a matrix of pixels with random RGB values and then bubble sorts them
across the entire matrix by pixel hue. It is very slow!
"""

import numpy as np
import cv2
from random import randint

def pixelsort(pixels=10):
    # Fill the matrix with black colour initially
    img = np.zeros((pixels,pixels,3), np.uint8)

    # Now fill it with random values and draw each line.
    # Sadly cv2.waitKey(1) (wait for a keypress for 1ms) is the shortest amount of
    # delay you can introduce between frames while still displaying an image.
    # So only display each line rather than each pixel (which is painfully slow).
    for x in img:
        cv2.imshow("PixelSort", img)
        cv2.waitKey(1)

        for y in x:
            y.itemset(0, randint(0,255))
            y.itemset(1, randint(0,255))
            y.itemset(2, randint(0,255))

    # Bubble sort the pixels
    sorted = False
    frame = 0
    while not sorted:
        sorted = True
        cv2.imshow("PixelSort", img)
        cv2.imwrite("output-%.5d.png" % frame, img)
        cv2.waitKey(1)

        for y in range(0,pixels):
            for x in range(0,pixels):
                # Don't fall off the end of the image
                if (x,y) == (pixels-1,pixels-1):
                    break

                # Pixels to compare
                (ax,ay) = (x,y)
                if x == pixels - 1:
                    (bx,by) = (0,y+1)
                else:
                    (bx,by) = (x+1,y)

                a_val = img[ay][ax].copy()
                b_val = img[by][bx].copy()

                #if ((a_val[2]<<16) + (a_val[1]<<8) + (a_val[0])) < ((b_val[2]<<16) + (b_val[1]<<8) + (b_val[0])):
                if hue(a_val) > hue(b_val):
                    img[ay][ax] = b_val
                    img[by][bx] = a_val
                    sorted = False
        frame += 1

def hue(elem):
    r = float(elem[2])
    g = float(elem[1])
    b = float(elem[0])

    delta = max(r,g,b) - min(r,g,b)
    if delta < 0.00001:
        return 0.0

    if r >= max(r,g,b):
        out = (g - b) / delta
    else:
        if g >= max(r,g,b):
            out = 2.0 + (b - r) / delta
        else:
            out = 4.0 + (r - g) / delta

    out *= 60.0
    if out < 0.0:
        out += 360.0
    
    return out

if __name__ == "__main__":
    cv2.namedWindow("PixelSort", cv2.WINDOW_AUTOSIZE)

    pixels = 200

    while True:
        pixelsort(pixels)
        print "Sorting finished"
        cv2.waitKey(0)

    cv2.destroyAllWindows()
