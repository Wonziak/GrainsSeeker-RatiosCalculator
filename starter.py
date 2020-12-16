import main
import cv2

if __name__ == '__main__':
    ratios = ['Haralick']
    statsRatiosToCalculateList = ['']
    colors = {
        'ferrite': (0, 255, 0),
        'bainite': (0, 0, 255),
        'martensite': (255, 0, 0),
    }
    image = cv2.imread('images/circle2.png')
    x, y = main.mainFunction(image, colors=colors, statistic_ratios=statsRatiosToCalculateList,
                             background='bainite')
    print(x, y)
