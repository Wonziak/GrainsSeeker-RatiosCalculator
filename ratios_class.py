import math
import RatiosConfig as rc


class Ratios:
    def __init__(self):
        self.Malinowska = float('inf')
        self.Mz = float('inf')
        self.Blair_Bliss = float('inf')
        self.Danielsson = float('inf')
        self.Haralick = float('inf')
        self.RLS = float('inf')
        self.RF = float('inf')
        self.RC1 = float('inf')
        self.RC2 = float('inf')
        self.RCom = float('inf')
        self.Lp1 = float('inf')
        self.Lp2 = float('inf')
        self.Lp3 = float('inf')
        self.calculatedRatiosDict = {}

    def malinowska(self):
        self.Malinowska = self.perimeter / (2 * math.sqrt(math.pi * self.area)) - 1

    def blair_bliss(self):
        self.Blair_Bliss = self.area / math.sqrt(2 * math.pi * self.distanceFromCenterPower)

    def danielsson(self):
        self.Danielsson = (self.area ** 3) / self.minDistanceFromEgdeSum

    def haralick(self):
        self.Haralick = math.sqrt((self.distanceFromCenter ** 2) / (self.area * self.distanceFromCenterPower - 1))

    def mz(self):
        self.Mz = (2 * math.sqrt(math.pi * self.area)) / self.perimeter

    def rls(self):
        self.RLS = self.perimeter / self.area

    def rf(self):
        self.RF = self.LH / self.LW

    def rc1(self):
        self.RC1 = math.sqrt(4 * self.area / math.pi)

    def rc2(self):
        self.RC2 = self.perimeter / math.pi

    def rcom(self):
        self.RCom = self.perimeter ** 2 / self.area

    def lp1(self):
        self.Lp1 = self.minDistaceCenterEdge / self.maxDistaceCenterEdge

    def lp2(self):
        self.Lp2 = self.maxDistancePoints / self.perimeter

    def lp3(self):
        # self.Lp3 = do zrobienia
        self.Lp3 = 0

    def calculateRatios(self):
        if 'malinowska' in rc.ratiosToCalculateList:
            self.malinowska()
            self.calculatedRatiosDict['malinowska'] = self.Malinowska
        if 'blair bliss' in rc.ratiosToCalculateList:
            self.blair_bliss()
            self.calculatedRatiosDict['blair bliss'] = self.Blair_Bliss
        if 'danielsson' in rc.ratiosToCalculateList:
            self.danielsson()
            self.calculatedRatiosDict['danielsson'] = self.Danielsson
        if 'haralick' in rc.ratiosToCalculateList:
            self.haralick()
            self.calculatedRatiosDict['haralick'] = self.Haralick
        if 'mz' in rc.ratiosToCalculateList:
            self.mz()
            self.calculatedRatiosDict['mz'] = self.Mz
        if 'rls' in rc.ratiosToCalculateList:
            self.rls()
            self.calculatedRatiosDict['rls'] = self.RLS
        if 'rf' in rc.ratiosToCalculateList:
            self.rf()
            self.calculatedRatiosDict['rf'] = self.RF
        if 'rc1' in rc.ratiosToCalculateList:
            self.rc1()
            self.calculatedRatiosDict['rc1'] = self.RC1
        if 'rc2' in rc.ratiosToCalculateList:
            self.rc2()
            self.calculatedRatiosDict['rc2'] = self.RC2
        if 'rcom' in rc.ratiosToCalculateList:
            self.rcom()
            self.calculatedRatiosDict['rcom'] = self.RCom
        if 'lp1' in rc.ratiosToCalculateList:
            self.lp1()
            self.calculatedRatiosDict['lp1'] = self.Lp1
        if 'lp2' in rc.ratiosToCalculateList:
            self.lp2()
            self.calculatedRatiosDict['lp2'] = self.Lp2
        if 'lp3' in rc.ratiosToCalculateList:
            self.lp3()
            self.calculatedRatiosDict['lp3'] = self.Lp3
