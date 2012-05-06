#!/usr/bin/env python

import sys
from cv2 import cv

def do_pyrdown(in_img, filter=cv.CV_GAUSSIAN_5x5):
  # verify image is halvable
  assert(in_img.width % 2 == 0 and in_img.height % 2 == 0)

  out_img = cv.CreateImage((in_img.width/2, in_img.height/2), in_img.depth, in_img.nChannels)
  cv.PyrDown(in_img, out_img, filter)
  return out_img

def do_capture(filename):
  # Set up the camera capture and grab a frame
  capture = cv.CreateCameraCapture(0)
  frame = cv.QueryFrame(capture)

  # transform the input twice
  out1 = do_pyrdown(frame)
  out2 = do_pyrdown(out1)

  # store to disk
  cv.SaveImage(filename, out2)

  # cleanup
  del(out1)
  del(out2)
  del(frame)
  del(capture)

if __name__ == "__main__":
  # check file is readable
  try:
    f = open(sys.argv[1], 'r')
  except IndexError:
    print >> sys.stderr, "You must supply a filename."
    sys.exit(1)
  except IOError:
    raise
  else:
    f.close()

  do_capture(sys.argv[1])
  sys.exit(0)
