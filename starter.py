import main
import cv2

if __name__ == '__main__':
    ratios = ['Malinowska']

    colors = {
        'ferrite': (0, 255, 0),
        'bainite': (0, 0, 255),
        'martensite': (255, 0, 0),
    }

    image = cv2.imread('images/halfRedHalfGreen.png')
    x, y = main.mainFunction(image, colors=colors, ratios=ratios, background='bainite')
    print(x, y)

