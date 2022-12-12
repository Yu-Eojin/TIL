import argparse
import os
from collections import deque
import random
import cv2
import numpy as np


def setup():
    parser = argparse.ArgumentParser()
    parser.add_argument('--img-path', '-i', dest='img_path', action='store', required=True, type=str,
                        help='Image FIle Path')
    parser.add_argument('--method', '-m',
                        help='Image processing method(gaussian(g), mean(m), median(md), threshold(t), adaptivethreshold(at))',
                        type=str, nargs='+', choices=['m', 'md', 'g', 't', 'at'])
    parser.add_argument('--save-path', '-s', help='Save Path', dest='save_path', type=str)
    parser.add_argument('--kernel', '-k', type=int, help='kernel size N(odd)', default=5)

    args = parser.parse_args()
    return args


def main(opt):
    img_path = opt.img_path
    filtered_img = cv2.imread(img_path)
    kernel_type = opt.method
    k = opt.kernel
    if k % 2 != 1:
        raise Exception('k is must be odd')
    for kt in kernel_type:
        # print(kt)
        if kt == 'm':
            kernel = np.ones((k, k)) / k ** 2
            filtered_img = cv2.filter2D(filtered_img, -1, kernel)
        elif kt == 'md':
            filtered_img = cv2.medianBlur(filtered_img, k)
        elif kt == 'g':
            filtered_img = cv2.GaussianBlur(filtered_img, (k, k), 2)
        elif kt == 't':
            if len(filtered_img.shape) == 3:
                filtered_img = cv2.cvtColor(filtered_img, cv2.COLOR_BGR2GRAY)
            _, filtered_img = cv2.threshold(filtered_img, 127, maxval=255, type=cv2.THRESH_BINARY)
        elif kt == 'at':
            if len(filtered_img.shape) == 3:
                filtered_img = cv2.cvtColor(filtered_img, cv2.COLOR_BGR2GRAY)
            filtered_img = cv2.adaptiveThreshold(filtered_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, k, 10)

    save_path = opt.save_path
    os.makedirs(save_path, exist_ok= True)
    file_name = f'({",".join(kernel_type)})filterd_{k}_' + os.path.split(img_path)[-1]
    cv2.imwrite(os.path.join(save_path, file_name), filtered_img)


if __name__ == '__main__':
    opt = setup()
    main(opt)
