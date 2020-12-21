from main import RatiosCalculator as Rc
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
    x, y = Rc().calculate_ratios(image=image, ratios=ratios, background='bainite', scale=1, colors=colors)
    print(x, y)
