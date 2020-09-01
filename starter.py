import numpy as np
import main
import cv2

ratios = ['Malinowska',
        'Blair Bliss',
        'Danielsson',
        'Haralick',
        'Mz',
        'RLS',
        'RF',
        'RC1',
        'RC2',
        'RCOM',
        'LP1',
        'LP2',
        'LP3']

image = cv2.imread('result2.png')
main.mainFunction(image, ratios)