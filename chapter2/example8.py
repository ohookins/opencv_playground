#!/usr/bin/env python

import sys
from cv2 import cv

def do_pyrdown(in_img, filter=cv.CV_GAUSSIAN_5x5):
  # verify image is halvable
  assert(in_img.width % 2 == 0 and in_img.height % 2 == 0)

  out_img = cv.CreateImage((in_img.width/2, in_img.height/2), in_img.depth, in_img.nChannels)
  cv.PyrDown(in_img, out_img, filter)
  return out_img

def do_canny(in_img, lowthresh, highthresh, aperture):
  if in_img.nChannels != 1:
    return 0 # only greyscale allowed

  out_img = cv.CreateImage((in_img.width, in_img.height), cv.IPL_DEPTH_8U, 1)
  cv.Canny(in_img, out_img, lowthresh, highthresh, aperture)
  return out_img

def get_images(image):
  cv.NamedWindow("Example8-in")
  cv.NamedWindow("Example8-out")

  # show the image
  cv.ShowImage("Example8-in", image)

  # transform the input
  out = do_pyrdown(image)
  out = do_pyrdown(out)
  out = do_canny(out, 10, 100, 3)

  # show the canny'd image
  cv.ShowImage("Example8-out", out)

  # destroy the temp image
  del(out)

  # wait for key then cleanup
  cv.WaitKey(0)
  cv.DestroyWindow("Example8-in")
  cv.DestroyWindow("Example8-out")

if __name__ == "__main__":
  # check file is readable
  try:
    f = open(sys.argv[1], 'r')
  except IndexError:
    print >> sys.stderr, "You must supply a filename."
    sys.exit(1)
  except IOError:
    raise
  else:
    f.close()

  get_images(cv.LoadImage(sys.argv[1], cv.CV_LOAD_IMAGE_GRAYSCALE))
  sys.exit(0)
