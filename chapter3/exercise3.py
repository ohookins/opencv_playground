#!/usr/bin/env python

import cv2
from cv2 import cv

def a(mat):
  """
  Draw a rectangle in the matrix. We can't use pointer logic so just use the
  built-in rectangle function.
  """
  # image, pt1, pt2, colour
  cv.Rectangle(mat, (20,5), (40,20), cv.CV_RGB(0,255,0))

def b(mat):
  """
  Display the matrix
  """
  cv.NamedWindow('Exercise3', cv.CV_WINDOW_AUTOSIZE)
  cv.ShowImage('Exercise3', mat)

  # Wait for a key press
  c = cv.WaitKey(0)

if __name__ == "__main__":
  # Create a 100x100 matrix with 3 channels of 8 bits
  mat = cv.CreateMat(100,100,cv2.CV_8UC3)
  cv.SetZero(mat)
  a(mat)
  b(mat)
