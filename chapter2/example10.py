#!/usr/bin/env python

import sys
from cv2 import cv

def convert_video(infile, outfile):
  capture = cv.CreateFileCapture(infile)

  if not capture:
    return None

  # initialize video read
  bgr_frame = cv.QueryFrame(capture)
  fps = cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FPS)
  size = (int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH)),
                       int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT)))

  writer = cv.CreateVideoWriter(outfile, cv.CV_FOURCC('M','P','4','2'), fps, size)
  logpolar_frame = cv.CreateImage(size, cv.IPL_DEPTH_8U, 3)

  # Convert the video. Note that this DOES NOT convert to greyscale.
  # It seems to convert to polar coordinates, which is not very useful.
  while True:
    bgr_frame = cv.QueryFrame(capture)
    if bgr_frame == None:
      break
    # cvPoint2D32f is also now just a tuple
    cv.LogPolar(bgr_frame, logpolar_frame, (
      (bgr_frame.width/2), (bgr_frame.height/2)), 40, cv.CV_INTER_LINEAR+cv.CV_WARP_FILL_OUTLIERS)

    cv.WriteFrame(writer, logpolar_frame)

  del(writer)
  del(logpolar_frame)
  del(capture)

if __name__ == "__main__":
  if len(sys.argv) == 3:
    # check files are readable
    try:
      f1 = open(sys.argv[1], 'r')
      f2 = open(sys.argv[2], 'r')
    except IOError:
     raise
    else:
      f1.close()
      f2.close()

    convert_video(sys.argv[1], sys.argv[2])
  sys.exit(0)
