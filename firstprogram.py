#!/usr/bin/python

import sys
from opencv import highgui

def show(filename):
  img =  highgui.cvLoadImage(filename)
  highgui.cvNamedWindow("Example1", highgui.CV_WINDOW_AUTOSIZE)
  highgui.cvShowImage("Example1", img)
  highgui.cvWaitKey(0)
  highgui.cvDestroyWindow("Example1")  

if __name__ == "__main__":
  show(sys.argv[1])
  sys.exit(0)
