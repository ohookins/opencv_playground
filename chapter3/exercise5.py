#!/usr/bin/python

import cv2
from cv2 import cv

def a(img):
  """
  Draw a pyramid using ROI and Set
  """
  border = 0
  limit = 210
  while (2*border) < limit:
    # set the ROI
    # (x,y,width,height)
    rect = (border,border,(limit-(2*border)),(limit-(2*border)))
    cv.SetImageROI(img, rect)

    # get the ROI and fill it
    cv.Set(img, (2*border))

    # Reset the ROI and increment the border
    cv.ResetImageROI(img)
    border += 10

def b(img):
  """
  Display the image
  """
  cv.NamedWindow('Exercise5', cv.CV_WINDOW_AUTOSIZE)
  cv.ShowImage('Exercise5', img)

  # Wait for a key press
  c = cv.WaitKey(0)

if __name__ == "__main__":
  # Create a 210x210 image with 1 channel of 8 bits
  img = cv.CreateImage((210,210),8,1)
  # image seems to be zeroed already
  a(img)
  b(img)
