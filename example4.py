#!/usr/bin/python

import sys
import opencv
from opencv.highgui import *

def example2_4(image):
  cvNamedWindow("Example4-in")
  cvNamedWindow("Example4-out")

  # show the image
  cvShowImage("Example4-in", image)

  # transform the input
  out = opencv.cvCreateImage(opencv.cvGetSize(image), opencv.IPL_DEPTH_8U, 3)
  opencv.cvSmooth(image, out, opencv.CV_GAUSSIAN, 3, 3)
  
  # show the smoothed image
  cvShowImage("Example4-out", out)

  opencv.cvReleaseImage(out)

  # wait for key then cleanup
  cvWaitKey(0)
  cvDestroyWindow("Example4-in")
  cvDestroyWindow("Example4-out")

if __name__ == "__main__":
  example2_4(cvLoadImage(sys.argv[1]))
  sys.exit(0)
