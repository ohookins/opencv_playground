#!/usr/bin/python

import sys
from cv2 import cv

def showavi(filename):
  cv.NamedWindow("Example2", cv.CV_WINDOW_AUTOSIZE)
  capture = cv.CreateFileCapture(filename)

  while True:
    frame = cv.QueryFrame(capture)
    if not frame:
      break
    cv.ShowImage("Example2", frame)

    c = cv.WaitKey(100)
    if c == 27: # escape key
      break

  #cv.ReleaseCapture(capture)
  # ReleaseCapture is no longer used
  del(capture)
  cv.DestroyWindow("Example2")

if __name__ == "__main__":
  try:
    f = open(sys.argv[1], 'r')
  except:
    raise
  else:
    f.close()

  showavi(sys.argv[1])
  sys.exit(0)
