#!/usr/bin/env python

import cv2
from cv2 import cv
from sys import stderr

try:
  from recordtype import recordtype
except ImportError:
  print >> stderr, """
Since CvRect is not exposed by the Python OpenCV library, we duplicate it
with a recordtype object. We want mutability and named attributes.
You'll need to install recordtype from pypi (e.g. with easy_install)."""
  exit(1)

CvRect = recordtype('CvRect', 'x y width height')

class Example1(object):
  """
  Container for the example code, mostly to avoid globals.
  """
  def __init__(self):
    self.box = CvRect(0,0,0,0)
    self.drawing_box = False

  def my_mouse_callback(self, event, x, y, flags, param):
    """
    Register a mouse callback. There is no prototype for it as in the book
    obviously, because this is Python.
    """
    image = param

    # Act on the event
    if event == cv.CV_EVENT_MOUSEMOVE:
      # If mouse movement caused the event, and we had already clicked,
      # update the box's dimensions.
      if self.drawing_box:
        self.box.width = x - self.box.x
        self.box.height = y - self.box.y

    elif event == cv.CV_EVENT_LBUTTONDOWN:
      # Set coords of the start of the box
      self.drawing_box = True
      self.box = CvRect(x, y, 0, 0)

    elif event == cv.CV_EVENT_LBUTTONUP:
      # Finish off the box, fix dimensions if we went backwards in the planes
      # and finally draw the box.
      self.drawing_box = False
      if self.box.width < 0:
        self.box.x += self.box.width
        self.box.width *= -1
      if self.box.height < 0:
        self.box.y += self.box.height
        self.box.height *= -1
      self.draw_box(image, self.box)

  def draw_box(self, img, rect):
    """
    Draw a single red box with the specified dimensions to the passed image.
    This is actually a pretty useless wrapper around cv.Rectangle.
    """
    cv.Rectangle(img, (rect.x, rect.y),
                (rect.x+rect.width,rect.y+rect.height),
                cv.CV_RGB(0xff, 0x00, 0x00))

  def run(self):
    """
    Draw boxes on the screen with the mouse.
    """
    # Define a small rectangle
    self.box = CvRect(-1,-1,0,0)

    # Create a small image, zero it and clone it.
    img =  cv.CreateImage((200,200),cv.IPL_DEPTH_8U,3)
    cv.SetZero(img)
    temp = cv.CloneImage(img)

    # Set up the window and the callback
    window = "Box Example"
    cv.NamedWindow(window, cv.CV_WINDOW_AUTOSIZE)
    cv.SetMouseCallback(window, self.my_mouse_callback, img)

    # main loop
    while True:
      temp = cv.CloneImage(img)

      # Draw the box into the temp image. This allows us to see the outline of
      # the box that we are in the process of drawing, but it only becomes
      # permanent when the mouse button is let go. More or less double
      # buffering.
      if self.drawing_box is True:
        self.draw_box(temp, self.box)

      # Display it.
      cv.ShowImage(window, temp)

      # Wait a small amount of time for a keypress
      c = cv.WaitKey(15)

      if c == 27: # escape key
        break

    # clean up after loop
    cv.DestroyWindow(window)

if __name__ == "__main__":
  Example1().run()
