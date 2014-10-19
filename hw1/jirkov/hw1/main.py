__author__ = 'sayon'

import numpy as np
import cv2

GAUSSIAN_SIZE = 3
GAUSSIAN_SIGMA = 15
LAPLASIAN_KERNEL_SIZE = [3,5,7]
LAPLASIAN_SCALE = 3
LAPLASIAN_DELTA = 0
LAPLASIAN_DEPTH = cv2.CV_16S

image_path = "../../text.bmp"

imgs = dict()
imgs['original'] = cv2.imread(image_path)


if not (imgs['original'] is None):
    imgs['gaussian'] = cv2.GaussianBlur(imgs['original'], (GAUSSIAN_SIZE,GAUSSIAN_SIZE), GAUSSIAN_SIGMA )
    imgs['gaussian, gsc'] = cv2.cvtColor(imgs['gaussian'], cv2.COLOR_RGB2GRAY)
    abs_dst = None
    for kersize in LAPLASIAN_KERNEL_SIZE:
        glap = cv2.Laplacian(imgs['gaussian, gsc'], LAPLASIAN_DEPTH, ksize=kersize, scale = LAPLASIAN_SCALE, delta=  LAPLASIAN_DELTA)
        imgs['lapl %10.3f' % kersize] = cv2.convertScaleAbs(glap)

    for name in imgs:
        cv2.imshow( name, imgs[name])

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print "Can not find file ", image_path