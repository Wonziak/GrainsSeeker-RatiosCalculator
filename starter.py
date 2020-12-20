import main
import cv2

if __name__ == '__main__':
    ratios = ['Haralick']
    statsRatiosToCalculateList = ['Linealpath']
    colors = {
        'ferrite': (0, 255, 0),
        'bainite': (0, 0, 255),
        'martensite': (255, 0, 0),
    }
    image = cv2.imread('images/circ.png')
    x, y = main.mainFunction(image, colors=colors, ratios=ratios, background='bainite', scale=1)
    print(x, y)
