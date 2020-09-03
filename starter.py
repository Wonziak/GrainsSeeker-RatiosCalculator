import numpy as np
import main
import cv2

ratios = ['Malinowska',
        'Blair Bliss',
        'Danielsson',
        'Haralick']

colors = {
    'bainite': (0, 255, 0),
    'martensite': (255, 0, 0)
}

image = cv2.imread('result2.png')
main.mainFunction(image, ratios, colors)
