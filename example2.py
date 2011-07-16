#!/usr/bin/python

import sys
from opencv import highgui

def showavi(filename):
  highgui.cvNamedWindow("Example2", highgui.CV_WINDOW_AUTOSIZE)
  capture = highgui.cvCreateFileCapture(filename)

  while True:
    frame = highgui.cvQueryFrame(capture)
    if not frame:
      break
    highgui.cvShowImage("Example2", frame)

    c = highgui.cvWaitKey(100)
    if c == '\x1b': # escape key
      break

  highgui.cvReleaseCapture(capture)
  highgui.cvDestroyWindow("Example2")

if __name__ == "__main__":
  showavi(sys.argv[1])
  sys.exit(0)
