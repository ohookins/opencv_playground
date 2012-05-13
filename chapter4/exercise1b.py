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

      self.write_original(frame, self.pane1)
      self.write_greyscale(frame, self.pane2)
      self.write_canny(frame, self.pane3)
      cv.ShowImage("Exercise1b", self.frame)

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
    (self.width,self.height) = (int(cv.GetCaptureProperty(self.cap, cv.CV_CAP_PROP_FRAME_WIDTH)),
                                int(cv.GetCaptureProperty(self.cap, cv.CV_CAP_PROP_FRAME_HEIGHT)))
    self.fps = cv.GetCaptureProperty(self.cap, cv.CV_CAP_PROP_FPS)

    # Set up the output window and the wider image to form the output buffer.
    # Set up sub rects to reference each "pane" of the buffer.
    cv.NamedWindow("Exercise1b", cv.CV_WINDOW_AUTOSIZE)
    self.frame = cv.CreateImage((self.width*3,self.height), cv.IPL_DEPTH_8U, 3)
    self.pane1 = cv.GetSubRect(self.frame, (0,0,self.width,self.height))
    self.pane2 = cv.GetSubRect(self.frame, (self.width,0,self.width,self.height))
    self.pane3 = cv.GetSubRect(self.frame, (self.width*2,0,self.width,self.height))

  def write_original(self, frame, output):
    """
    Display the unaltered frame.
    """
    cv.Copy(frame, output)

  def write_greyscale(self, orig, output):
    """
    Convert the frame from (assumed) RGB to greyscale and display it.
    """
    temp1 = cv.CreateImage(cv.GetSize(orig), cv.IPL_DEPTH_8U, 1)
    temp2 = cv.CreateImage(cv.GetSize(orig), cv.IPL_DEPTH_8U, 3)
    cv.CvtColor(orig, temp1, cv2.COLOR_RGB2GRAY)
    cv.CvtColor(temp1, temp2, cv2.COLOR_GRAY2RGB)
    cv.Copy(temp2, output)

  def write_canny(self, orig, output):
    """
    Display the frame with Canny edge detection.
    """
    temp1 = cv.CreateImage(cv.GetSize(orig), cv.IPL_DEPTH_8U, 1)
    temp2 = cv.CreateImage(cv.GetSize(orig), cv.IPL_DEPTH_8U, 3)
    canny = cv.CreateImage(cv.GetSize(orig), cv.IPL_DEPTH_8U, 1)
    cv.CvtColor(orig, temp1, cv2.COLOR_RGB2GRAY)
    cv.Canny(temp1, canny, 0.5, 1.0, 5)
    cv.CvtColor(canny, temp2, cv2.COLOR_GRAY2RGB)
    cv.Copy(temp2, output)


if __name__ == "__main__":
  if len(sys.argv) != 2:
    print >> sys.stderr, "Usage: %s <filename>" % sys.argv[0]
    sys.exit(1)
  else:
    Exercise1(sys.argv[1]).run()
