#!/usr/bin/python

from opencv import cv

if __name__ == "__main__":
  print """
  The FileStorage routines do not work at all in python opencv, so don't bother.

  You also cannot use marshal or pickle to store SwigPyObject objects, so there
  is no easy way of storing the native data types.
  """
