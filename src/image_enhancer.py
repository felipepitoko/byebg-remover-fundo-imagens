import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def adjust_brightness_contrast(image, alpha, beta):
    return cv2.addWeighted(image, alpha, image, 0, beta)

def read_image(image_path):
    image = cv2.imread(image_path)
    return image

def enhace_all_images():
    for image in os.listdir('inputs'):
        image_path = os.path.join('inputs', image)
        image = read_image(image_path)
        image = adjust_brightness_contrast(image, 1.5, 0)
        image = sharpen_image(image)
        image_path = os.path.join('outputs', image)
        cv2.imwrite(image_path, image)
        
def sharpen_image(image):
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])
    return cv2.filter2D(image, -1, kernel)

def enhance_one_image(image_path):
    image = read_image(image_path)
    image = adjust_brightness_contrast(image, 1.5, 0)
    image = sharpen_image(image)
    image_path = os.path.join('outputs', image)
    cv2.imwrite(image_path, image)