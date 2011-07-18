#!/usr/bin/python

import sys
from opencv import cvSize, IPL_DEPTH_8U, cvCreateImage, cvLogPolar, cvPoint2D32f, CV_INTER_LINEAR, CV_WARP_FILL_OUTLIERS, cvReleaseImage
from opencv.highgui import *

def convert_video(infile, outfile):
  capture = cvCreateFileCapture(infile)

  if not capture:
    return None

  # initialize video read
  bgr_frame = cvQueryFrame(capture)
  fps = cvGetCaptureProperty(capture, CV_CAP_PROP_FPS)
  size = cvSize(int(cvGetCaptureProperty(capture, CV_CAP_PROP_FRAME_WIDTH)),
                       int(cvGetCaptureProperty(capture, CV_CAP_PROP_FRAME_HEIGHT)))

  writer = cvCreateVideoWriter(outfile, CV_FOURCC('M','P','4','2'), fps, size)
  logpolar_frame = cvCreateImage(size, IPL_DEPTH_8U, 3)

  # Convert the video. Note that this DOES NOT convert to greyscale.
  # It seems to convert to polar coordinates, which is not very useful.
  while True:
    bgr_frame = cvQueryFrame(capture)
    if bgr_frame == None:
      break
    cvLogPolar(bgr_frame, logpolar_frame, cvPoint2D32f(
      (bgr_frame.width/2), (bgr_frame.height/2)), 40, CV_INTER_LINEAR+CV_WARP_FILL_OUTLIERS)

    cvWriteFrame(writer, logpolar_frame)

  cvReleaseVideoWriter(writer)
  cvReleaseImage(logpolar_frame)
  cvReleaseCapture(capture)

if __name__ == "__main__":
  if len(sys.argv) == 3:
    convert_video(sys.argv[1], sys.argv[2])
  sys.exit(0)
