#!/usr/bin/python

import sys
import opencv
from opencv.highgui import *

def do_pyrdown(in_img, filter=opencv.CV_GAUSSIAN_5x5):
  # verify image is halvable
  assert(in_img.width % 2 == 0 and in_img.height % 2 == 0)

  out_img = opencv.cvCreateImage(opencv.cvSize(in_img.width/2, in_img.height/2), in_img.depth, in_img.nChannels)
  opencv.cvPyrDown(in_img, out_img, filter)
  return out_img

def example2_4(image):
  cvNamedWindow("Example5-in")
  cvNamedWindow("Example5-out")

  # show the image
  cvShowImage("Example5-in", image)

  # transform the input
  out = do_pyrdown(image)
  
  # show the reduced image
  cvShowImage("Example5-out", out)

  opencv.cvReleaseImage(out)

  # wait for key then cleanup
  cvWaitKey(0)
  cvDestroyWindow("Example5-in")
  cvDestroyWindow("Example5-out")

if __name__ == "__main__":
  example2_4(cvLoadImage(sys.argv[1]))
  sys.exit(0)
