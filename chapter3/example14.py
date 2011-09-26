#!/usr/bin/python

import sys
from cv2 import cv

if __name__ == "__main__":
  """
alphablend <imageA> <image B> <x> <y> <width> <height>
           <alpha> <beta>
  """
  if len(sys.argv) == 9:
    src1 = cv.LoadImage(sys.argv[1], cv.CV_LOAD_IMAGE_COLOR)
    src2 = cv.LoadImage(sys.argv[2], cv.CV_LOAD_IMAGE_COLOR)
    if (src1 is not None) and (src2 is not None):
      x = int(sys.argv[3])
      y = int(sys.argv[4])
      width = int(sys.argv[5])
      height = int(sys.argv[6])
      alpha = float(sys.argv[7])
      beta = float(sys.argv[8])

      cv.SetImageROI(src1, (x, y, width, height))
      cv.SetImageROI(src2, (0, 0, width, height))
      cv.AddWeighted(src1, alpha, src2, beta, 0.0, src1)
      cv.ResetImageROI(src1)
      cv.NamedWindow('Alpha_blend', 1)
      cv.ShowImage('Alpha_blend', src1)
      cv.WaitKey()
