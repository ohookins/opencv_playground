#!/usr/bin/env python

import sys
from cv2 import cv

if __name__ == "__main__":
  if len(sys.argv) == 7:
    src = cv.LoadImage(sys.argv[1])
    if src is not None:
      x = int(sys.argv[2])
      y = int(sys.argv[3])
      width = int(sys.argv[4])
      height = int(sys.argv[5])
      add = int(sys.argv[6])

      # cvRect is just expressed as a tuple
      cv.SetImageROI(src, (x,y,width,height))
      cv.AddS(src, cv.Scalar(add), src)
      cv.ResetImageROI(src)
      cv.NamedWindow('Roi_Add', 1)
      cv.ShowImage('Roi_Add', src)
      cv.WaitKey()
