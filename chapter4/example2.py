#!/usr/bin/env python

import cv2
from cv2 import cv

class Example2(object):
  """
  Container for the example code, mostly to avoid globals.
  """
  def __init__(self):
    self.switch_value = 0

  def switch_callback(self, position):
    """
    Turn the switch off or on based on change in position.
    """
    if position == 0:
      self.switch_off()
    else:
      self.switch_on()

  def switch_off(self):
    """
    Function run by turning the switch off"
    """
    print "OFF"

  def switch_on(self):
    """
    Function run by turning the switch on"
    """
    print "ON"

  def run(self):
    """
    Show the use of sliders as two-position switches.
    """
    windowname = "Demo Window"
    cv.NamedWindow(windowname, cv.CV_WINDOW_AUTOSIZE)

    # Create the trackbar
    cv.CreateTrackbar("Switch", windowname, self.switch_value, 1, self.switch_callback)

    # Loop
    while True:
      if cv.WaitKey(15) == 27: break

if __name__ == "__main__":
  Example2().run()
