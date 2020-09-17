import numpy as np
import main
import cv2

ratios = ['Malinowska']

colors = {
    'ferrite': (0, 0, 255),
    'bainite': (0, 255, 0),
    'martensite': (255, 0, 0)
}

image = cv2.imread('circle2.png')
x, y = main.mainFunction(image, colors=colors, ratios=ratios, background='ferrite')
print(x, y)
