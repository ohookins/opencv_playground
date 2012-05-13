#!/usr/bin/env python

import cv2
from cv2 import cv

if __name__ == "__main__":
  filename = './picture.avi'
  cap = cv.CreateFileCapture(filename)

  # It is supposed to come out as a double (long), but Python interprets it as
  # a float for some reason.
  fourcc_long = long(cv.GetCaptureProperty(cap, cv.CV_CAP_PROP_FOURCC))

  # There's got to be a better way of doing this:
  fourcc = chr((fourcc_long & 0x000000FF)) + chr((fourcc_long & 0x0000FF00) >> 8 ) + chr((fourcc_long & 0x00FF0000) >> 16) + chr((fourcc_long & 0xFF000000) >> 24)
  print "FourCC code of %s is %s" % (filename, fourcc)
