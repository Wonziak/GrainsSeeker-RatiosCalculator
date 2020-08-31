import cv2
import numpy as np
import ImageConfig
import grain_class as grain
import DataGatherer as dg
import numpy as np
import matplotlib.pyplot as plt

grains = []

def findContoursAndCalculateRatios(layer, phase):
    ret, thresh = cv2.threshold(layer, 1, 255, 0)
    allcontours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    allcontoursx = []
    allcontoursy = []
    contours = []
    for contour in range(len(allcontours)):
        allcontoursx.append(allcontours[contour][0][0][0])
        allcontoursy.append(allcontours[contour][0][0][1])
        ImageConfig.drawCountour(allcontours[contour])

    for number in range(len(allcontours)):
        if int(layer[allcontoursy[number]+1, allcontoursx[number]+1]) == 255:
            contours.append(allcontours[number])

    for i in range(len(contours)):
        grains.append(grain.Grain(contours[i], phase))





# PRZEROSOWANIE OBRAZKA ZGODNIE Z KOLORAMI
ImageConfig.image = cv2.imread('circle3.png')
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
    layer = PhaseLayers[:, :, index]
    # cv2.imshow('bl', layer)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    index = index + 1


# DLA KAŻDEJ FAZY WYWOŁANIE FUNKCJI SZUKAJĄCEJ ZIAREN
for phase in range(len(ImageConfig.colors_map)):
    phaseName = list(ImageConfig.colors_map.keys())
    findContoursAndCalculateRatios(PhaseLayers[:, :, phase], phaseName[phase])

print(len(grains))
print(grains[4].minDistaceCenterEdge, grains[4].maxDistaceCenterEdge, grains[4].LW, grains[4].LH)
dg.createSeriesFromRatios(grains)
dg.createHistograms(len(grains))