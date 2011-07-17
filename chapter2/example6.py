#!/usr/bin/python

import sys
import opencv
from opencv.highgui import *

def do_canny(in_img, lowthresh, highthresh, aperture):
  if in_img.nChannels != 1:
    return 0 # only greyscale allowed

  out_img = opencv.cvCreateImage(opencv.cvSize(in_img.width, in_img.height), opencv.IPL_DEPTH_8U, 1)
  opencv.cvCanny(in_img, out_img, lowthresh, highthresh, aperture)
  return out_img

def get_images(image):
  cvNamedWindow("Example6-in")
  cvNamedWindow("Example6-out")

  # show the image
  cvShowImage("Example6-in", image)

  # transform the input
  out = do_canny(image, 0.1, 1.0, 3)
  if out == 0:
    print "error during canny"
  
  # show the canny'd image
  cvShowImage("Example6-out", out)

  opencv.cvReleaseImage(out)

  # wait for key then cleanup
  cvWaitKey(0)
  cvDestroyWindow("Example6-in")
  cvDestroyWindow("Example6-out")

if __name__ == "__main__":
  get_images(cvLoadImage(sys.argv[1], CV_LOAD_IMAGE_GRAYSCALE))
  sys.exit(0)
