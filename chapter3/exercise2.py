#!/usr/bin/env python

import cv2
from cv2 import cv

def a(mat):
  """
  Draw a circle in the matrix
  """
  # image, center, radius, colour
  cv.Circle(mat, (50,50), 30, cv.CV_RGB(200,200,200))

def b(mat):
  """
  Display the matrix
  """
  cv.NamedWindow('Exercise2', cv.CV_WINDOW_AUTOSIZE)
  cv.ShowImage('Exercise2', mat)

  # Wait for a key press
  c = cv.WaitKey(0)

if __name__ == "__main__":
  # Create a 100x100 matrix with 3 channels of 8 bits
  mat = cv.CreateMat(100,100,cv2.CV_8UC3)
  cv.SetZero(mat)
  a(mat)
  b(mat)
