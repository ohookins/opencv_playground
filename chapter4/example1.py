#!/usr/bin/python

import cv2
from cv2 import cv

box = None
drawing_box = False

def my_mouse_callback(event, x, y, flags, param):
  """
  Register a mouse callback. There is no prototype for it as in the book
  obviously, because this is Python.
  """
  global box
  global drawing_box
  image = param

  # Act on the event
  if event == cv.CV_EVENT_MOUSEMOVE:
    # If mouse movement caused the event, and we had already clicked,
    # update the box's dimensions.
    if drawing_box:
      # Tuples are immutable
      box = (box[0], box[1], x - box[0], y - box[1])

  elif event == cv.CV_EVENT_LBUTTONDOWN:
    # Set coords of the start of the box
    drawing_box = True
    box = (x, y, 0, 0)

  elif event == cv.CV_EVENT_LBUTTONUP:
    # Finish off the box, fix dimensions if we went backwards in the planes
    # and finally draw the box.
    drawing_box = False
    if box[2] < 0:
      box = (box[0] + box[2], box[1], -box[2], box[3])
    if box[3] < 0:
      box = (box[0], box[1] + box[3], box[2], -box[3])
    draw_box(image, box)

def draw_box(img, rect):
  """
  Draw a single, red box.
  """
  cv.Rectangle(img, (rect[0], rect[1]),
              (rect[0]+rect[2],rect[1]+rect[3]),
              cv.CV_RGB(0xff, 0x00, 0x00))

def run():
  """
  Draw boxes on the screen with the mouse.
  """
  global box

  # Define a small rectangle
  box = (-1,-1,0,0)

  # Create a small image, zero it and clone it.
  img =  cv.CreateImage((200,200),cv.IPL_DEPTH_8U,3)
  cv.SetZero(img)
  temp = cv.CloneImage(img)

  # Set up the window and the callback
  window = "Box Example"
  cv.NamedWindow(window, cv.CV_WINDOW_AUTOSIZE)
  cv.SetMouseCallback(window, my_mouse_callback, img)

  # main loop
  while True:
    temp = cv.CloneImage(img)

    # Draw the box into the temp image.
    if drawing_box is True:
      draw_box(temp, box)

    # Display it
    cv.ShowImage(window, temp)

    # Wait a small amount of time for a keypress
    c = cv.WaitKey(15)

    if c == 27: # escape key
      break

  # clean up after loop
  cv.DestroyWindow(window)

if __name__ == "__main__":
  run()
