#!/usr/bin/python

from opencv import cv

if __name__ == "__main__":
  print """
  The FileStorage routines do not work at all in python opencv, so don't bother.
  """
  #fs = cv.cvOpenFileStorage('cfg.yaml', None, cv.CV_STORAGE_WRITE)
  #cv.cvWriteInt(fs, 'frame_count', 10)
  #cv.cvStartWriteStruct(fs, 'frame_size', cv.CV_NODE_SEQ)
  #cv.cvWriteInt(fs, 0, 320)
  #cv.cvWriteInt(fs, 0, 200)
  #cv.cvEndWriteStruct(fs)
  #cv.cvWrite(fs, 'color_cvt_matrix', cv.cmatrix)
  #cv.cvReleaseFileStorage(fs)
  #del fs
