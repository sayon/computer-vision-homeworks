import cv2
import numpy
from numpy.fft import fft2, ifft2, fftshift, ifftshift



def fourier(image, zeroing_size):
    fshift = fftshift(fft2(image))

    # hpf
    rows, cols = image.shape
    center_row, center_col = rows / 2, cols / 2
    fshift[center_row - zeroing_size:center_row + zeroing_size, center_col - zeroing_size:center_col + zeroing_size] = 0


    # inversion

    img_back = ifft2(ifftshift(fshift))
    img_back = numpy.abs(img_back)
    cv2.imshow("fourier", img_back)


def laplacian(image, kernel_size):
    laplacian = cv2.Laplacian(image, cv2.CV_32F, ksize=kernel_size)
    cv2.imshow("laplacian", laplacian)


img = cv2.imread("../../mandril.bmp", cv2.CV_LOAD_IMAGE_GRAYSCALE)
fourier(img, 30)
laplacian(img, 3)
cv2.waitKey(0)
cv2.destroyAllWindows()
