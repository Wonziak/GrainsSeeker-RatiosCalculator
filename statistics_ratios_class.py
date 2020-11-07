import ImageConfig as ic
import itertools
import grain_class as gc
import numpy as np


class Statistics:
    def __init__(self):
        self.imageArea = ic.height * ic.width
        self.borderNeighboursCountRatio = {}
        self.dispertionPhases = {}
        self.onePointProbability = {}
        self.linealPath = {}
        self.angleZero = {}
        self.angle45 = {}
        self.angle90 = {}

    def blr(self):
        colors = list(ic.colors_map.keys())
        colorsDict = {v: k for k, v in ic.colors_map.items()}

        for pair in itertools.combinations(colors, 2):
            combination = pair[0] + pair[1]
            self.borderNeighboursCountRatio[combination] = 0

        for i in range(ic.height):
            for j in range(ic.width - 1):
                color = [ic.image[i, j, 2], ic.image[i, j, 1], ic.image[i, j, 0]]
                nbcolorright = [ic.image[i, j + 1, 2], ic.image[i, j + 1, 1], ic.image[i, j + 1, 0]]
                if tuple(color) in colorsDict.keys() and tuple(nbcolorright) in colorsDict.keys():
                    phasename = colorsDict[tuple(color)]
                    nbrightphasename = colorsDict[tuple(nbcolorright)]
                    if phasename + nbrightphasename in self.borderNeighboursCountRatio.keys():
                        self.borderNeighboursCountRatio[phasename + nbrightphasename] += 1
                    if nbrightphasename + phasename in self.borderNeighboursCountRatio.keys():
                        self.borderNeighboursCountRatio[nbrightphasename + phasename] += 1

        for i in range(ic.height - 1):
            for j in range(ic.width):
                color = [ic.image[i, j, 2], ic.image[i, j, 1], ic.image[i, j, 0]]
                nbcolorunder = [ic.image[i + 1, j, 2], ic.image[i + 1, j, 1], ic.image[i + 1, j, 0]]
                if tuple(color) in colorsDict.keys() and tuple(nbcolorunder) in colorsDict.keys():
                    phasename = colorsDict[tuple(color)]
                    nbcolorunderphasename = colorsDict[tuple(nbcolorunder)]
                    if phasename + nbcolorunderphasename in self.borderNeighboursCountRatio.keys():
                        self.borderNeighboursCountRatio[phasename + nbcolorunderphasename] += 1
                    if nbcolorunderphasename + phasename in self.borderNeighboursCountRatio.keys():
                        self.borderNeighboursCountRatio[nbcolorunderphasename + phasename] += 1
        allborderpixels = sum(list(self.borderNeighboursCountRatio.values()))
        if allborderpixels != 0:
            for key, value in self.borderNeighboursCountRatio.items():
                self.borderNeighboursCountRatio[key] = value / allborderpixels

    def dispertion(self, grains, scale):
        area = self.imageArea * (scale ** 2)
        for phases in ic.colors_map.keys():
            self.dispertionPhases[phases] = 0
        for gc.Grain in grains:
            self.dispertionPhases[gc.Grain.phase] += 1
        for key, value in self.dispertionPhases.items():
            self.dispertionPhases[key] = value / area

    def onePointProb(self):
        colorsDict = {v: k for k, v in ic.colors_map.items()}
        for phase in ic.colors_map.keys():
            self.onePointProbability[phase] = 0
        for i in range(ic.height):
            for j in range(ic.width):
                color = (ic.image[i, j, 2], ic.image[i, j, 1], ic.image[i, j, 0])
                if color in colorsDict.keys():
                    phasename = colorsDict[color]
                    self.onePointProbability[phasename] += 1
        for key, value in self.onePointProbability.items():
            self.onePointProbability[key] = value / self.imageArea

    def linealpath(self):
        for phase in ic.colors_map.keys():
            self.linealPath[phase] = {'angleZero': np.zeros((ic.width,), dtype=float),
                                      'angle90': np.zeros((ic.height,), dtype=float),
                                      'angle45': np.zeros((ic.height,), dtype=float)}
        colorsDict = {v: k for k, v in ic.colors_map.items()}
        rng = np.random.default_rng()
        xCoordinates = rng.choice(ic.width, 50)
        yCoordinates = rng.choice(ic.height, 50)
        for point in range(50):
            x = xCoordinates[point]
            y = yCoordinates[point]
            xyColor = (ic.image[y, x, 2], ic.image[y, x, 1], ic.image[y, x, 0])
            for pointAngleZero in range(ic.width - 1):
                pointAngleZero = pointAngleZero + 1
                pointToCheck = x + pointAngleZero
                if pointToCheck >= ic.width:
                    pointToCheck = pointToCheck - ic.width
                pointToCheckColor = (ic.image[y, pointToCheck, 2], ic.image[y, pointToCheck, 1],
                                     ic.image[y, pointToCheck, 0])
                if xyColor[0] == pointToCheckColor[0] and xyColor[1] == pointToCheckColor[1] and xyColor[2] == \
                        pointToCheckColor[2]:
                    self.linealPath[colorsDict[xyColor]]['angleZero'][pointAngleZero] += 1
                else:
                    break
            for pointAngle90 in range(ic.height - 1):
                pointAngle90 = pointAngle90 + 1
                pointToCheck = y + pointAngle90
                if pointToCheck >= ic.height:
                    pointToCheck = pointToCheck - ic.height
                pointToCheckColor = (ic.image[pointToCheck, x, 2], ic.image[pointToCheck, x, 1],
                                     ic.image[pointToCheck, x, 0])
                if xyColor[0] == pointToCheckColor[0] and xyColor[1] == pointToCheckColor[1] and xyColor[2] == \
                        pointToCheckColor[2]:
                    self.linealPath[colorsDict[xyColor]]['angle90'][pointAngle90] += 1
                else:
                    break
            for pointAngle45 in range(ic.height - 1):
                pointAngle45 = pointAngle45 + 1
                pointToCheckY = y - pointAngle45
                pointToCheckX = x + pointAngle45
                if pointToCheckX >= ic.width:
                    pointToCheckX = pointToCheckX - ic.width
                if pointToCheckY < 0:
                    pointToCheckY = pointToCheckY + ic.height - 1
                pointToCheckColor = (
                ic.image[pointToCheckY, pointToCheckX, 2], ic.image[pointToCheckY, pointToCheckX, 1],
                ic.image[pointToCheckY, pointToCheckX, 0])
                if xyColor[0] == pointToCheckColor[0] and xyColor[1] == pointToCheckColor[1] and xyColor[2] == \
                        pointToCheckColor[2]:
                    self.linealPath[colorsDict[xyColor]]['angle45'][pointAngle45] += 1
                else:
                    break
        for phase in ic.colors_map.keys():
            self.linealPath[phase]['angleZero'] = np.delete(self.linealPath[phase]['angleZero'], 0)
            self.linealPath[phase]['angle45'] = np.delete(self.linealPath[phase]['angle45'], 0)
            self.linealPath[phase]['angle90'] = np.delete(self.linealPath[phase]['angle90'], 0)

    def returnRatios(self):
        return {'borderNeighbour': self.borderNeighboursCountRatio,
                'dispertionPhases': self.dispertionPhases,
                'onePointprobability': self.onePointProbability,
                'lineal-path': self.linealPath
                }
