import ImageConfig as ic
import itertools
import grain_class as gc


class Statistics:
    def __init__(self):
        self.borderNeighboursCount = {}
        self.dispertionPhases = {}

    def blr(self):
        colors = list(ic.colors_map.keys())
        colorsDict = {v: k for k, v in ic.colors_map.items()}

        for pair in itertools.combinations(colors, 2):
            combination = pair[0] + pair[1]
            self.borderNeighboursCount[combination] = 0

        for i in range(ic.height):
            for j in range(ic.width - 1):
                color = [ic.image[i, j, 2], ic.image[i, j, 1], ic.image[i, j, 0]]
                nbcolorright = [ic.image[i, j + 1, 2], ic.image[i, j + 1, 1], ic.image[i, j + 1, 0]]
                if tuple(color) in colorsDict.keys() and tuple(nbcolorright) in colorsDict.keys():
                    phasename = colorsDict[tuple(color)]
                    nbrightphasename = colorsDict[tuple(nbcolorright)]
                    if phasename + nbrightphasename in self.borderNeighboursCount.keys():
                        self.borderNeighboursCount[phasename + nbrightphasename] += 1
                    if nbrightphasename + phasename in self.borderNeighboursCount.keys():
                        self.borderNeighboursCount[nbrightphasename + phasename] += 1

        for i in range(ic.height - 1):
            for j in range(ic.width):
                color = [ic.image[i, j, 2], ic.image[i, j, 1], ic.image[i, j, 0]]
                nbcolorunder = [ic.image[i + 1, j, 2], ic.image[i + 1, j, 1], ic.image[i + 1, j, 0]]
                if tuple(color) in colorsDict.keys() and tuple(nbcolorunder) in colorsDict.keys():
                    phasename = colorsDict[tuple(color)]
                    nbcolorunderphasename = colorsDict[tuple(nbcolorunder)]
                    if phasename + nbcolorunderphasename in self.borderNeighboursCount.keys():
                        self.borderNeighboursCount[phasename + nbcolorunderphasename] += 1
                    if nbcolorunderphasename + phasename in self.borderNeighboursCount.keys():
                        self.borderNeighboursCount[nbcolorunderphasename + phasename] += 1
        allborderpixels = sum(list(self.borderNeighboursCount.values()))
        if allborderpixels != 0:
            for key, value in self.borderNeighboursCount.items():
                self.borderNeighboursCount[key] = value / allborderpixels

    def dispertion(self, grains, scale):
        area = ic.width * ic.height * (scale ** 2)
        for phases in ic.colors_map.keys():
            self.dispertionPhases[phases] = 0
        for gc.Grain in grains:
            self.dispertionPhases[gc.Grain.phase] += 1
        for key, value in self.dispertionPhases.items():
            self.dispertionPhases[key] = value / area

    def returnRatios(self):
        return {'borderNeighbour': self.borderNeighboursCount,
                'dispertionPhases': self.dispertionPhases}
