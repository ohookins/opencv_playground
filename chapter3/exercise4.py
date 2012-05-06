#!/usr/bin/env python

import cv2
from cv2 import cv

def a(mat):
  """
  Draw a square in the matrix. We can't use pointer logic so just use the
  built-in rectangle function.
  """
  pt1 = (20,5)
  pt2 = (40,20)

  # Figure out which is the shortest side to use for the square
  if abs(pt1[0]-pt2[0]) > abs(pt1[1]-pt2[1]):
    longer_side = 0
    shorter_side = 1
  else:
    longer_side = 1
    shorter_side = 0

  # Place the square in the middle of the rectangle.
  # I'm sure this is not completely correct.
  side_length = abs(pt1[shorter_side]-pt2[shorter_side])
  start_x = ((abs(pt1[0]-pt2[0])-side_length)/2)+pt1[0]
  start_y = ((abs(pt1[1]-pt2[1])-side_length)/2)+pt1[1]

  # image, pt1, pt2, colour
  cv.Rectangle(mat, (start_x,start_y), pt2, cv.CV_RGB(0,255,0))

def b(mat):
  """
  Display the matrix
  """
  cv.NamedWindow('Exercise4', cv.CV_WINDOW_AUTOSIZE)
  cv.ShowImage('Exercise4', mat)

  # Wait for a key press
  c = cv.WaitKey(0)

if __name__ == "__main__":
  # Create a 100x100 matrix with 3 channels of 8 bits
  mat = cv.CreateMat(100,100,cv2.CV_8UC3)
  cv.SetZero(mat)
  a(mat)
  b(mat)
