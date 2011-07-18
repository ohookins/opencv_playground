#!/usr/bin/python

import sys
from opencv import CV_GAUSSIAN_5x5, cvCreateImage, cvSize, cvPyrDown
from opencv.highgui import cvCreateCameraCapture, cvQueryFrame, cvShowImage, cvNamedWindow, CV_WINDOW_AUTOSIZE, cvWaitKey

def do_pyrdown(in_img, filter=CV_GAUSSIAN_5x5):
  # verify image is halvable
  assert(in_img.width % 2 == 0 and in_img.height % 2 == 0)

  out_img = cvCreateImage(cvSize(in_img.width/2, in_img.height/2), in_img.depth, in_img.nChannels)
  cvPyrDown(in_img, out_img, filter)
  return out_img

def do_capture():
  # Set up the camera capture
  capture = cvCreateCameraCapture(0)

  # Create a window
  cvNamedWindow("Exercise4", CV_WINDOW_AUTOSIZE)

  while True:
    # Capture a frame and shrink it twice
    out = cvQueryFrame(capture)
    if out == None:
      next
    out = do_pyrdown(out)
    out = do_pyrdown(out)
    cvShowImage("Exercise4", out)

    # Check for esc key
    c = cvWaitKey(33)
    if c == '\x1b':
      return(0)

if __name__ == "__main__":
  do_capture()
  sys.exit(0)
