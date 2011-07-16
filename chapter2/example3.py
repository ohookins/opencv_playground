#!/usr/bin/python

import sys
from opencv import highgui

capture = None
slider_pos = 0

def on_trackbar_slide(position):
  highgui.cvSetCaptureProperty(capture, highgui.CV_CAP_PROP_POS_FRAMES, position)

def showavi(filename):
  highgui.cvNamedWindow("Example3", highgui.CV_WINDOW_AUTOSIZE)
  global capture
  capture = highgui.cvCreateFileCapture(filename)

  frames = int(highgui.cvGetCaptureProperty(capture, highgui.CV_CAP_PROP_FRAME_COUNT))
  
  if frames != 0:
    highgui.cvCreateTrackbar("Position", "Example3", slider_pos, frames, on_trackbar_slide)
    
  while True:
    frame = highgui.cvQueryFrame(capture)
    if not frame:
      break
    highgui.cvShowImage("Example3", frame)

    c = highgui.cvWaitKey(100)
    if c == '\x1b': # escape key
      break

  highgui.cvReleaseCapture(capture)
  highgui.cvDestroyWindow("Example3")

if __name__ == "__main__":
  showavi(sys.argv[1])
  sys.exit(0)
