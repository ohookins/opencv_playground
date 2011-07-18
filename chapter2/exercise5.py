#!/usr/bin/python

import sys
from opencv import CV_GAUSSIAN_5x5, cvCreateImage, cvSize, cvPyrDown, cvResize
from opencv.highgui import cvCreateCameraCapture, cvQueryFrame, cvShowImage, cvNamedWindow, CV_WINDOW_AUTOSIZE, cvWaitKey, cvCreateTrackbar, cvGetTrackbarPos

def dummy(tmp):
    pass

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
  cvNamedWindow("Exercise5", CV_WINDOW_AUTOSIZE)

  # Set up the trackbar
  slider_pos = 0
  cvCreateTrackbar("Reduction", "Exercise5", slider_pos, 4, dummy)

  while True:
    # Capture a frame
    frame = cvQueryFrame(capture)
    if frame == None:
      continue

    # Make sure it is divisible by up to 8
    out = cvCreateImage(cvSize((frame.width/8)*8, (frame.height/8)*8), frame.depth, frame.nChannels)
    cvResize(frame, out)

    # Reduce the image by pyramid depending on the slider position
    slider_pos = cvGetTrackbarPos("Reduction", "Exercise5")
    if slider_pos != 0:
      for i in range(slider_pos):
        out = do_pyrdown(out)
    cvShowImage("Exercise5", out)

    # Check for esc key
    c = cvWaitKey(33)
    if c == '\x1b':
      return(0)

if __name__ == "__main__":
  do_capture()
  sys.exit(0)
