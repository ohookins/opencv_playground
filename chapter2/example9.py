#!/usr/bin/env python

import sys
from cv2 import cv

def showcam(filename=None):
  if filename != None:
    capture = cv.CreateFileCapture(filename)
  else:
    capture = cv.CreateCameraCapture(-1)

  while True:
    frame = cv.QueryFrame(capture)
    if not frame:
      if not filename:
        next
      else:
        break
    cv.ShowImage("Example9", frame)

    c = cv.WaitKey(30)
    if c == 27: # escape key
      break

  del(capture)
  cv.DestroyWindow("Example9")

if __name__ == "__main__":
  if len(sys.argv) == 2:
    # check file is readable
    try:
      f = open(sys.argv[1], 'r')
    except IOError:
      raise
    else:
      f.close()

    showcam(sys.argv[1])
  else:
    showcam()
  sys.exit(0)
