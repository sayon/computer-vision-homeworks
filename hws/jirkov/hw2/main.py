__author__ = 'sayon'

import cv2
import numpy as np


GAUSSIAN_SIZE = 3
GAUSSIAN_SIGMA = 1
LAPLASIAN_KERNEL_SIZE = 3
LAPLASIAN_SCALE = 1
LAPLASIAN_DELTA = 0
LAPLASIAN_DEPTH = cv2.CV_16S
DILATE_KERNEL_SIZE = 3
ERODE_KERNEL_SIZE = 3
image_path = "../../text.bmp"

imgs = dict()
imgs['original'] = cv2.imread(image_path)

if not (imgs['original'] is None):
    imgs['gaussian'] = cv2.GaussianBlur(imgs['original'], (GAUSSIAN_SIZE, GAUSSIAN_SIZE), GAUSSIAN_SIGMA)
    abs_dst = None
    glap = cv2.Laplacian(imgs['gaussian'], LAPLASIAN_DEPTH, ksize=LAPLASIAN_KERNEL_SIZE, scale=LAPLASIAN_SCALE,
                         delta=LAPLASIAN_DELTA)
    laplname = 'lapl %10.3f' % LAPLASIAN_KERNEL_SIZE
    imgs[laplname] = cv2.convertScaleAbs(glap)

    dilatekernel = np.ones((DILATE_KERNEL_SIZE, DILATE_KERNEL_SIZE), np.uint8)
    erodekernel = np.ones((ERODE_KERNEL_SIZE, ERODE_KERNEL_SIZE), np.uint8)

    imgs['gsc'] = cv2.cvtColor(imgs[laplname], cv2.COLOR_BGR2GRAY)

    imgs['dilated'] = cv2.dilate(imgs['gsc'], dilatekernel)
    imgs['erode'] = cv2.erode(imgs['dilated'], erodekernel, iterations=2)
    ret, bw = cv2.threshold(imgs['erode'], 120, 255, 0)

    (h, w) = imgs['original'].shape[:2]

    mask = np.zeros((h + 2, w + 2), np.uint8)
    imgs['rects'] = imgs['original'].copy()


    for x in xrange(0, w):
        for y in xrange(0, h):
            if bw[y][x] == 255\
                    :
                v, rect = cv2.floodFill(bw, None, seedPoint = (x, y), newVal = (100, 100, 100))
                print v, " ",  rect
                cv2.rectangle(imgs['rects'], rect[:2], (rect[0] + rect[2], rect[1] + rect[3]), 1000)
    for name in imgs:
        cv2.imshow(name, imgs[name])
    cv2.imshow("bw", bw)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print    "Can not find file ", image_path