#!/usr/bin/python

import sys
from cv2 import cv

if __name__ == "__main__":
  """ Brief example of saving/loading matrices to/from files """
  mat = cv.CreateMat(5, 5, cv.CV_32FC1)
  cv.SetIdentity(mat)
  print mat
  cv.Save('my_matrix.xml', mat)

  mat2 = cv.Load('my_matrix.xml')
  print mat2
