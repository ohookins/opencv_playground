#!/usr/bin/python

import sys
from opencv import cv
from opencv import highgui

if __name__ == "__main__":
  if len(sys.argv) == 7:
    src = highgui.cvLoadImage(sys.argv[1])
    if src is not None:
      x = int(sys.argv[2])
      y = int(sys.argv[3])
      width = int(sys.argv[4])
      height = int(sys.argv[5])
      add = int(sys.argv[6])

      #cv.cvSetImageROI(src, highgui.cvRect(x,y,width,height))
      # workaround for missing ROI functions in python opencv libraries
      sub = cv.cvGetSubRect(src, cv.cvRect(x, y, width, height))
      cv.cvAddS(sub, cv.cvScalar(add),sub)
      #highgui.cvResetImageROI(src)
      highgui.cvNamedWindow('Roi_Add', 1)
      highgui.cvShowImage('Roi_Add', src)
      highgui.cvWaitKey()
