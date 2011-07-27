#!/usr/bin/python

import sys
from opencv import highgui

def showcam(filename=None):
  if filename != None:
    capture = highgui.cvCreateFileCapture(filename)
  else:
    capture = highgui.cvCreateCameraCapture(-1)

  while True:
    frame = highgui.cvQueryFrame(capture)
    if not frame:
      next
    highgui.cvShowImage("Example9", frame)

    c = highgui.cvWaitKey(30)
    if c == '\x1b': # escape key
      break

  highgui.cvReleaseCapture(capture)
  highgui.cvDestroyWindow("Example9")

if __name__ == "__main__":
  if len(sys.argv) == 2:
    showcam(sys.argv[1])
  else:
    showcam()
  sys.exit(0)
