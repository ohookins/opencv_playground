#!/usr/bin/python

import sys
from cv2 import cv

def show(filename):
  img =  cv.LoadImage(filename)
  cv.NamedWindow("Example1", cv.CV_WINDOW_AUTOSIZE)
  cv.ShowImage("Example1", img)
  cv.WaitKey(0)
  cv.DestroyWindow("Example1")

if __name__ == "__main__":
  show(sys.argv[1])
  sys.exit(0)
