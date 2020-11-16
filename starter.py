import main
import cv2

if __name__ == '__main__':
    ratios = ['Malinowska']
    statsRatiosToCalculateList = ['BorderNeighbour',
                                  'Dispersion',
                                  'OnePointProbability']
    colors = {
        'ferrite': (0, 255, 0),
        'bainite': (0, 0, 255),
        'martensite': (255, 0, 0),
    }

    image = cv2.imread('images/circ.png')
    x, y = main.mainFunction(image, colors=colors, ratios=ratios, statistic_ratios=statsRatiosToCalculateList,
                             background='bainite')
    print(x, y)
