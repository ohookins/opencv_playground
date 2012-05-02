#!/usr/bin/python

import cv2
from cv2 import cv
import random

def a():
  """
  Run a value through some math functions.
  """
  myvalue = -227.12345

  # Abs()
  # There MUST be a better way of doing this, using a scalar or something.
  a = cv.CreateMat(1,1,cv2.CV_32FC1)
  a[0,0] = myvalue
  b = cv.CreateMat(1,1,cv2.CV_32FC1)
  cv.Abs(a, b)
  print "Absolute value of %f is %f" % (a[0,0], b[0,0])

  # Round()
  print "Rounded value of %f is %i" % (myvalue, cv.Round(myvalue))

  # Ceil()
  print "Ceil value of %f is %i" % (myvalue, cv.Ceil(myvalue))

  # Floor()
  print "Floor value of %f is %i" % (myvalue, cv.Floor(myvalue))

def b():
  """
  Random numbers. cv.RNG is not very random so we help it along with the python
  random library.
  """
  print "Random int: %i" % cv.RandInt(cv.RNG(random.randint(1,1000000)))
  print "Random float: %f" % cv.RandReal(cv.RNG(random.randint(1,1000000)))

def c():
  """
  CvPoint2D32f and CvPoint are just tuples. No point writing exercises.
  """

def d():
  """
  ditto as for c()
  """

if __name__ == "__main__":
  a()
  b()
  c()
  d()
