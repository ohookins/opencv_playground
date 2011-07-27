#!/usr/bin/python

import sys
from opencv import cv
from opencv import highgui

if __name__ == "__main__":
  """
alphablend <imageA> <image B> <x> <y> <width> <height>
           <alpha> <beta>
  """
  if len(sys.argv) == 9:
    src1 = highgui.cvLoadImage(sys.argv[1], highgui.CV_LOAD_IMAGE_COLOR)
    src2 = highgui.cvLoadImage(sys.argv[2], highgui.CV_LOAD_IMAGE_COLOR)
    if (src1 is not None) and (src2 is not None):
      x = int(sys.argv[3])
      y = int(sys.argv[4])
      width = int(sys.argv[5])
      height = int(sys.argv[6])
      alpha = float(sys.argv[7])
      beta = float(sys.argv[8])

      # Again have to use subrect to emulate an ROI
      sub1 = cv.cvGetSubRect(src1, cv.cvRect(x, y, width, height))
      sub2 = cv.cvGetSubRect(src2, cv.cvRect(0, 0, width, height))
      cv.cvAddWeighted(sub1, alpha, sub2, beta, 0.0, sub1)
      
      highgui.cvNamedWindow('Alpha_blend', 1)
      highgui.cvShowImage('Alpha_blend', src1)
      highgui.cvWaitKey()
