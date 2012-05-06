#!/usr/bin/env python

import sys
from cv2 import cv

def do_pyrdown(in_img, filter=cv.CV_GAUSSIAN_5x5):
  # verify image is halvable
  assert(in_img.width % 2 == 0 and in_img.height % 2 == 0)

  # cvGetSize is now just a tuple
  out_img = cv.CreateImage((in_img.width/2, in_img.height/2), in_img.depth, in_img.nChannels)
  cv.PyrDown(in_img, out_img, filter)
  return out_img

def example2_4(image):
  cv.NamedWindow("Example5-in")
  cv.NamedWindow("Example5-out")

  # show the image
  cv.ShowImage("Example5-in", image)

  # transform the input
  out = do_pyrdown(image)

  # show the reduced image
  cv.ShowImage("Example5-out", out)

  #cv.ReleaseImage(out)
  del(out)

  # wait for key then cleanup
  cv.WaitKey(0)
  cv.DestroyWindow("Example5-in")
  cv.DestroyWindow("Example5-out")

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

  example2_4(cv.LoadImage(sys.argv[1]))
  sys.exit(0)
