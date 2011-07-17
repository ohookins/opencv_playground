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
  cvNamedWindow("Example7-in")
  cvNamedWindow("Example7-out")

  # show the image
  cvShowImage("Example7-in", image)

  # transform the input
  img1 = do_pyrdown(image)
  img2 = do_pyrdown(img1)
  img3 = do_canny(img2, 10, 100, 3)
  
  # show the canny'd image
  cvShowImage("Example7-out", img3)

  opencv.cvReleaseImage(img1)
  opencv.cvReleaseImage(img2)
  opencv.cvReleaseImage(img3)

  # wait for key then cleanup
  cvWaitKey(0)
  cvDestroyWindow("Example7-in")
  cvDestroyWindow("Example7-out")

if __name__ == "__main__":
  get_images(cvLoadImage(sys.argv[1], CV_LOAD_IMAGE_GRAYSCALE))
  sys.exit(0)
