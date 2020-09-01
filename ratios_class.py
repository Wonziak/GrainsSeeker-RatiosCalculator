import math
import RatiosConfig as rc


class Ratios:
    def __init__(self):
        self.Malinowska = 0
        self.Mz = 0
        self.Blair_Bliss = 0
        self.Danielsson = 0
        self.Haralick = 0
        self.RLS = 0
        self.RF = 0
        self.RC1 = 0
        self.RC2 = 0
        self.RCom = 0
        self.Lp1 = 0
        self.Lp2 = 0
        self.Lp3 = 0

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
        if not rc.ratiosToCalculateList:
            self.malinowska()
            self.blair_bliss()
            self.danielsson()
            self.haralick()
            self.mz()
            self.rls()
            self.rf()
            self.rc1()
            self.rc2()
            self.rcom()
            self.lp1()
            self.lp2()
            self.lp3()
            print('here')
        else:
            if 'malinowska' in rc.ratiosToCalculateList:
                self.malinowska()
            if 'blair bliss' in rc.ratiosToCalculateList:
                self.blair_bliss()
            if 'danielsson' in rc.ratiosToCalculateList:
                self.danielsson()
            if 'haralick' in rc.ratiosToCalculateList:
                self.haralick()
            if 'mz' in rc.ratiosToCalculateList:
                self.mz()
            if 'rls' in rc.ratiosToCalculateList:
                self.rls()
            if 'rf' in rc.ratiosToCalculateList:
                self.rf()
            if 'rc1' in rc.ratiosToCalculateList:
                self.rc1()
            if 'rc2' in rc.ratiosToCalculateList:
                self.rc2()
            if 'rcom' in rc.ratiosToCalculateList:
                self.rcom()
            if 'lp1' in rc.ratiosToCalculateList:
                self.lp1()
            if 'lp2' in rc.ratiosToCalculateList:
                self.lp2()
            if 'lp3' in rc.ratiosToCalculateList:
                self.lp3()
