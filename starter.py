import main
import cv2

if __name__ == '__main__':
    ratios = ['Malinowska']

    colors = {
        'ferrite': (0, 0, 255),
        'bainite': (0, 255, 0),
        'martensite': (255, 0, 0)
    }

    image = cv2.imread('circlesPer.png')
    x, y = main.mainFunction(image, colors=colors, ratios=ratios, background='ferrite', periodical=False)
    print(x, y)

