#!/usr/bin/env python

import cv2
from cv2 import cv
import sys
import os

class Exercise1(object):
  """
  Read in a video, and perform some real-time video processing on it.
  """

  def __init__(self, filename):
    """
    Rudimentary pre-flight checks
    """
    self.filename = filename
    if not os.path.exists(filename):
      print >> sys.stderr, "%s doesn't exist" % filename
      sys.exit(1)

  def run(self):
    """
    Wrap around the main parts of the processing.
    """
    self.setup_display()
    wait_period = int(1000.0/self.fps)

    # Loop over frames in the video
    while True:
      frame = cv.QueryFrame(self.cap)
      if frame == None:
        break

      self.display_original(frame)
      self.display_greyscale(frame)
      self.display_canny(frame)

      # Esc quits
      c = cv.WaitKey(wait_period)
      if c == 27:
        break

    del(self.cap)
    sys.exit(1)

  def setup_display(self):
    """
    Read video source and setup the outputs for it.
    """
    self.cap = cv.CaptureFromFile(self.filename)
    (self.width,self.height) = (cv.GetCaptureProperty(self.cap, cv.CV_CAP_PROP_FRAME_WIDTH),
                                cv.GetCaptureProperty(self.cap, cv.CV_CAP_PROP_FRAME_HEIGHT))
    self.fps = cv.GetCaptureProperty(self.cap, cv.CV_CAP_PROP_FPS)

    # Set up the output windows
    cv.NamedWindow("Original", cv.CV_WINDOW_AUTOSIZE)
    cv.NamedWindow("Greyscale", cv.CV_WINDOW_AUTOSIZE)
    cv.NamedWindow("Edge Detect", cv.CV_WINDOW_AUTOSIZE)

  def display_original(self, frame):
    """
    Display the unaltered frame.
    """
    cv.ShowImage("Original", frame)

  def display_greyscale(self, orig):
    """
    Convert the frame from (assumed) RGB to greyscale and display it.
    """
    frame = cv.CreateImage(cv.GetSize(orig), cv.IPL_DEPTH_8U, 1)
    cv.CvtColor(orig, frame, cv2.COLOR_RGB2GRAY)
    cv.ShowImage("Greyscale", frame)

  def display_canny(self, orig):
    """
    Display the frame with Canny edge detection.
    """
    greyscale = cv.CreateImage(cv.GetSize(orig), cv.IPL_DEPTH_8U, 1)
    frame = cv.CreateImage(cv.GetSize(orig), cv.IPL_DEPTH_8U, 1)
    cv.CvtColor(orig, greyscale, cv2.COLOR_RGB2GRAY)
    cv.Canny(greyscale, frame, 0.5, 1.0, 5)
    cv.ShowImage("Edge Detect", frame)


if __name__ == "__main__":
  if len(sys.argv) != 2:
    print >> sys.stderr, "Usage: %s <filename>" % sys.argv[0]
    sys.exit(1)
  else:
    Exercise1(sys.argv[1]).run()
