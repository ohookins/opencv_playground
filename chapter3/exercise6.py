#!/usr/bin/python

import cv2
from cv2 import cv

def a(img):
  """
  Create two image headers from the image and draw rectangles in them.
  """
  header1 = cv.CreateImageHeader(cv.GetSize(img),img.depth,img.nChannels)
  header2 = cv.CreateImageHeader(cv.GetSize(img),img.depth,img.nChannels)
  #(header1.width,header1.height) = (20,30)
  #(header2.width,header2.height) = (20,30)

  # Hmm, what to do here. We can't set pointers into the image from these
  # headers. Something with ctypes?

def b(img):
  """
  Display the image
  """
  cv.NamedWindow('Exercise6', cv.CV_WINDOW_AUTOSIZE)
  cv.ShowImage('Exercise6', img)

  # Wait for a key press
  c = cv.WaitKey(0)

if __name__ == "__main__":
  # Load an example image
  img = cv.LoadImage('picture.jpg')
  a(img)
  b(img)
