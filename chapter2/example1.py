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
  # check file is readable
  try:
    f = open(sys.argv[1], 'r')
  except IndexError:
    print >> sys.stderr, "You must supply a filename."
    sys.exit(1)
  except IOError:
    raise
  else:
    f.close()

  show(sys.argv[1])
  sys.exit(0)
