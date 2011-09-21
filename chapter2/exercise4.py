#!/usr/bin/python

import sys
from cv2 import cv

def do_pyrdown(in_img, filter=cv.CV_GAUSSIAN_5x5):
  # verify image is halvable
  assert(in_img.width % 2 == 0 and in_img.height % 2 == 0)

  out_img = cv.CreateImage((in_img.width/2, in_img.height/2), in_img.depth, in_img.nChannels)
  cv.PyrDown(in_img, out_img, filter)
  return out_img

def do_capture():
  # Set up the camera capture
  capture = cv.CreateCameraCapture(0)

  # Create a window
  cv.NamedWindow("Exercise4", cv.CV_WINDOW_AUTOSIZE)

  while True:
    # Capture a frame and shrink it twice
    out = cv.QueryFrame(capture)
    if out == None:
      next
    out = do_pyrdown(out)
    out = do_pyrdown(out)
    cv.ShowImage("Exercise4", out)

    # Check for esc key
    c = cv.WaitKey(33)
    if c == 27:
      return(0)

if __name__ == "__main__":
  do_capture()
  sys.exit(0)
