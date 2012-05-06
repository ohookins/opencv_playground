#!/usr/bin/env python

import cv2
from cv2 import cv

def run(img):
  """
  Extract the channels
  """
  # If we pass None objects to cv.Split it will throw an assertion error,
  # so create three new matrices to hold the output.
  red = cv.CreateMat(img.height, img.width, cv2.CV_8UC1)
  green = cv.CreateMat(img.height, img.width, cv2.CV_8UC1)
  blue = cv.CreateMat(img.height, img.width, cv2.CV_8UC1)

  # Split the img into three channels
  cv.Split(img, red, green, blue, None)

  # Display the green channel (assuming RGB order)
  display(green, 'Green Channel')

  # Clone the green channel twice
  (clone1,clone2) = (cv.CloneMat(green),cv.CloneMat(green))

  # Find the green channel's min and max
  (minval,maxval,minloc,maxloc) = cv.MinMaxLoc(green)

  # Set the first clone to be some kind of threshold value
  # and the second to zeroes.
  thresh = int((maxval-minval)/2.0)
  cv.Set(clone1, thresh)
  cv.SetZero(clone2)

  # Then generate a mask from the original green channel and the matrix
  # of threshold values.
  cv.Cmp(green, clone1, clone2, cv.CV_CMP_GE)

  # Subtract half the threshold value from elements that exceed the threshold
  # (i.e. those matching the mask we generated).
  cv.SubS(green, thresh/2, green, clone2)
  display(green, 'Thresholded green')

def display(img, name):
  """
  Display the image
  """
  cv.NamedWindow(name, cv.CV_WINDOW_AUTOSIZE)
  cv.ShowImage(name, img)

  # Wait for a key press
  c = cv.WaitKey(0)

if __name__ == "__main__":
  # Load an example image
  img = cv.LoadImage('picture.jpg')
  run(img)
