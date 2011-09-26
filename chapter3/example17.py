#!/usr/bin/python

import cv2

if __name__ == "__main__":
  fs = cv2.FileStorage('cfg.xml', cv2.FILE_STORAGE_WRITE)
  # the python file storage interface is more or less useless
  fs.release()
