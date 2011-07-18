#!/usr/bin/python

import sys
from opencv import CV_GAUSSIAN_5x5, cvCreateImage, cvSize, cvPyrDown
from opencv.highgui import cvCreateCameraCapture, cvQueryFrame, cvSaveImage

def do_pyrdown(in_img, filter=CV_GAUSSIAN_5x5):
  # verify image is halvable
  assert(in_img.width % 2 == 0 and in_img.height % 2 == 0)

  out_img = cvCreateImage(cvSize(in_img.width/2, in_img.height/2), in_img.depth, in_img.nChannels)
  cvPyrDown(in_img, out_img, filter)
  return out_img

def do_capture(filename):
  # Set up the camera capture and grab a frame
  capture = cvCreateCameraCapture(0)
  frame = cvQueryFrame(capture)

  # transform the input twice
  out1 = do_pyrdown(frame)
  out2 = do_pyrdown(out1)

  # store to disk
  cvSaveImage(filename, out2)

if __name__ == "__main__":
  do_capture(sys.argv[1])
  sys.exit(0)
