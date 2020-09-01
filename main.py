import cv2
import ImageConfig
import RatiosConfig as rc
import grain_class as grain
import DataGatherer as dg
import numpy as np
import matplotlib.pyplot as plt

grains = []

def findContoursAndCalculateRatios(layer, phase):
    ret, thresh = cv2.threshold(layer, 1, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # for i in range(len(contours)):
    #     ImageConfig.drawCountour(contours[i])

    for i in range(len(contours)):
        print(i, 'ziarno z fazy:', phase)
        grains.append(grain.Grain(contours[i], phase))



def mainFunction(image, ratios=[], colors=ImageConfig.colors_map):
    # PRZEROSOWANIE OBRAZKA ZGODNIE Z KOLORAMI
    rc.ratiosToCalculateList = ratios
    rc.tolowercase()
    ImageConfig.image = image
    ImageConfig.height, ImageConfig.width = ImageConfig.image.shape[:2]

    PhaseLayers = np.zeros((ImageConfig.height, ImageConfig.width, len(ImageConfig.colors_map)), np.uint8)
    print(PhaseLayers.shape)
    index = 0
    for color in ImageConfig.colors_map.values():
        for i in range(ImageConfig.width):
            for j in range(ImageConfig.height):
                if ImageConfig.image[j, i, 0] == color[2] and ImageConfig.image[j, i, 1] == color[1] and ImageConfig.image[
                    j, i, 2] == color[0]:  # BGR nie RGB
                    PhaseLayers[j, i, index] = 255
        # layer = PhaseLayers[:, :, index]
        # cv2.imshow('bl', layer)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        index = index + 1


    # DLA KAŻDEJ FAZY WYWOŁANIE FUNKCJI SZUKAJĄCEJ ZIAREN
    for phase in range(len(ImageConfig.colors_map)):
        phaseName = list(ImageConfig.colors_map.keys())
        findContoursAndCalculateRatios(PhaseLayers[:, :, phase], phaseName[phase])

    print(len(grains))
    print(grains[1].minDistaceCenterEdge, grains[1].maxDistaceCenterEdge, grains[1].LW, grains[1].LH)
    dg.createSeriesFromRatios(grains)
    dg.createHistograms(len(grains))