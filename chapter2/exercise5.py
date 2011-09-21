#!/usr/bin/python

import sys
from cv2 import cv

slider_pos = 0

def update_slider(pos):
  global slider_pos
  slider_pos = pos

def do_pyrdown(in_img, filter=cv.CV_GAUSSIAN_5x5):
  # verify image is halvable
  assert(in_img.width % 2 == 0 and in_img.height % 2 == 0)

  out_img = cv.CreateImage((in_img.width/2, in_img.height/2), in_img.depth, in_img.nChannels)
  cv.PyrDown(in_img, out_img, filter)
  return out_img

def do_capture():
  global slider_pos

  # Set up the camera capture
  capture = cv.CreateCameraCapture(0)

  # Create a window
  cv.NamedWindow("Exercise5", cv.CV_WINDOW_AUTOSIZE)

  # Set up the trackbar
  slider_pos = 0
  cv.CreateTrackbar("Reduction", "Exercise5", slider_pos, 4, update_slider)

  while True:
    # Capture a frame
    frame = cv.QueryFrame(capture)
    if frame == None:
      continue

    # Make sure it is divisible by up to 8
    out = cv.CreateImage(((frame.width/8)*8, (frame.height/8)*8), frame.depth, frame.nChannels)
    cv.Resize(frame, out)

    # Reduce the image by pyramid depending on the slider position
    if slider_pos != 0:
      for i in range(slider_pos):
        out = do_pyrdown(out)
    cv.ShowImage("Exercise5", out)

    # Check for esc key
    c = cv.WaitKey(33)
    if c == 27:
      return(0)

if __name__ == "__main__":
  do_capture()
  sys.exit(0)
