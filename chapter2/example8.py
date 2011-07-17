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

def do_canny(in_img, lowthresh, highthresh, aperture):
  if in_img.nChannels != 1:
    return 0 # only greyscale allowed

  out_img = opencv.cvCreateImage(opencv.cvSize(in_img.width, in_img.height), opencv.IPL_DEPTH_8U, 1)
  opencv.cvCanny(in_img, out_img, lowthresh, highthresh, aperture)
  return out_img

def get_images(image):
  cvNamedWindow("Example8-in")
  cvNamedWindow("Example8-out")

  # show the image
  cvShowImage("Example8-in", image)

  # transform the input
  out = do_pyrdown(image)
  out = do_pyrdown(out)
  out = do_canny(out, 10, 100, 3)
  
  # show the canny'd image
  cvShowImage("Example8-out", out)

  opencv.cvReleaseImage(out)

  # wait for key then cleanup
  cvWaitKey(0)
  cvDestroyWindow("Example8-in")
  cvDestroyWindow("Example8-out")

if __name__ == "__main__":
  get_images(cvLoadImage(sys.argv[1], CV_LOAD_IMAGE_GRAYSCALE))
  sys.exit(0)
