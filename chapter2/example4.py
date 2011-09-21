#!/usr/bin/python

import sys
from cv2 import cv

def example2_4(image):
  cv.NamedWindow("Example4-in")
  cv.NamedWindow("Example4-out")

  # show the image
  cv.ShowImage("Example4-in", image)

  # transform the input
  out = cv.CreateImage(cv.GetSize(image), cv.IPL_DEPTH_8U, 3)
  cv.Smooth(image, out, cv.CV_GAUSSIAN, 3, 3)

  # show the smoothed image
  cv.ShowImage("Example4-out", out)

  #cv.ReleaseImage(out)
  del(out)

  # wait for key then cleanup
  cv.WaitKey(0)
  cv.DestroyWindow("Example4-in")
  cv.DestroyWindow("Example4-out")

if __name__ == "__main__":
  example2_4(cv.LoadImage(sys.argv[1]))
  sys.exit(0)
