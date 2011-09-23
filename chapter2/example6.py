#!/usr/bin/python

import sys
from cv2 import cv

def do_canny(in_img, lowthresh, highthresh, aperture):
  if in_img.nChannels != 1:
    return 0 # only greyscale allowed

  out_img = cv.CreateImage((in_img.width, in_img.height), cv.IPL_DEPTH_8U, 1)
  cv.Canny(in_img, out_img, lowthresh, highthresh, aperture)
  return out_img

def get_images(image):
  cv.NamedWindow("Example6-in")
  cv.NamedWindow("Example6-out")

  # show the image
  cv.ShowImage("Example6-in", image)

  # transform the input
  out = do_canny(image, 0.1, 1.0, 3)
  if out == 0:
    print "error during canny"

  # show the canny'd image
  cv.ShowImage("Example6-out", out)


  # wait for key then cleanup
  cv.WaitKey(0)
  del(out)
  cv.DestroyWindow("Example6-in")
  cv.DestroyWindow("Example6-out")

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
