#!/usr/bin/python

import sys
from cv2 import cv

capture = None
slider_pos = 0

def on_trackbar_slide(position):
  global slider_pos
  cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_POS_FRAMES, position)
  slider_pos = position

def showavi(filename):
  cv.NamedWindow("Example3", cv.CV_WINDOW_AUTOSIZE)
  global capture, slider_pos
  capture = cv.CreateFileCapture(filename)

  frames = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_COUNT))

  if frames != 0:
    cv.CreateTrackbar("Position", "Example3", slider_pos, frames, on_trackbar_slide)

  while True:
    frame = cv.QueryFrame(capture)
    if not frame:
      break
    cv.ShowImage("Example3", frame)

    # update the trackbar position
    slider_pos += 1
    if slider_pos % 10 == 0: # updating on every frame causes video to lag
      cv.SetTrackbarPos("Position", "Example3", slider_pos)

    c = cv.WaitKey(100)
    if c == 27: # escape key
      break

  #cv.ReleaseCapture(capture)
  del(capture)
  cv.DestroyWindow("Example3")

if __name__ == "__main__":
  # check file is readable, as cv.CreateFileCapture does not
  try:
    f = open(sys.argv[1], 'r')
  except:
    raise
  else:
    f.close()

  showavi(sys.argv[1])
  sys.exit(0)
