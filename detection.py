import cv2
import numpy as np
from matplotlib import pyplot as plt

# just a list for future refrence
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

METHOD = 'cv2.TM_CCOEFF'

def detect(target, source):
    img = cv2.imread(source,0)
    img2 = img.copy()
    template = cv2.imread(target,0)
    w, h = template.shape[::-1]

    img = img2.copy()
    method = eval(METHOD)

    # Apply template Matching
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # find center of rec
    centerX = (top_left[0] + bottom_right[0]) / 2
    centerY = (top_left[1] + bottom_right[1]) / 2

    return centerX, centerY