import numpy as np
import ImageConfig
import cv2
import math


class Grain:
    def __init__(self, edge, phase):
        self.edge = edge
        self.phase = phase
        self.domain = []
        self.perimeter = len(edge) # obwód - długość
        self.area = 0
        self.Malinowska = 0
        self.Mz = 0
        self.Blair_Bliss = 0
        self.Danielsson = 0
        self.Haralick = 0
        self.getArea()
        self.centerOfMass = []
        self.distanceFromCenterPower = 0
        self.distanceFromCenter = 0
        self.minDistanceFromEgdeSum = 0
        self.minDistaceCenterEdge = 0
        self.maxDistaceCenterEdge = 0
        self.maxDistancePoints = 0
        self.LH = 0
        self.LW = 0
        self.RLS = 0
        self.RF = 0
        self.RC1 = 0
        self.RC2 = 0
        self.RCom = 0
        self.Lp1 = 0
        self.Lp2 = 0
        self.Lp3 = 0
        self.calculateRatios()

    def getArea(self):  #powierzchnia to domain(współrzędne), area to ilosc punktow
        domain = []
        for i in range(ImageConfig.width):
            for j in range(ImageConfig.height):
                if cv2.pointPolygonTest(self.edge, (i, j), measureDist=False) >= 0:
                    domain.append([i, j])
        self.domain = domain
        self.area = len(self.domain)

    def findCoM(self):  # srodek ciezkosci
        allx = 0
        ally = 0
        for i in range(self.area):
            allx += self.domain[i][0]  # suma wspołrzędnych x pola
            ally += self.domain[i][1]  # suma wspołrzędnych y pola
        meanX = int(allx / self.area)
        meanY = int(ally / self.area)
        self.centerOfMass.append(meanX)
        self.centerOfMass.append(meanY)

    def calculateRatios(self):
        self.findCoM()
        self.calculateDistancesSumFromCenter()
        self.calculateHeightWidth()
        # self.calculateMaxMinFromCenter()
        # self.calculateMaxDistanceGrain()
        self.malinowska()
        self.blair_bliss()
        self.findMinDistSum()
        self.danielsson()
        self.haralic()
        self.mz()
        self.RLS = self.perimeter/self.area
        self.RF = self.LH/self.LW
        self.RC1 = math.sqrt(4*self.area/math.pi)
        self.RC2 = self.perimeter/math.pi
        self.RCom = self.perimeter**2/self.area
        # self.Lp1 = self.minDistaceCenterEdge/self.maxDistaceCenterEdge
        self.Lp2 = self.maxDistancePoints/self.perimeter
        # self.Lp3 = do zrobienia

    def malinowska(self):
        self.Malinowska = self.perimeter / (2 * math.sqrt(math.pi * self.area)) - 1

    def blair_bliss(self):
        self.Blair_Bliss = self.area / math.sqrt(2 * math.pi * self.distanceFromCenterPower)

    def danielsson(self):
        self.Danielsson = (self.area**3)/self.minDistanceFromEgdeSum

    def haralic(self):
        self.Haralick = math.sqrt((self.distanceFromCenter**2)/(self.area*self.distanceFromCenterPower -1))

    def mz(self):
        self.Mz = (2 * math.sqrt(math.pi * self.area))/self.perimeter

    def calculateDistancesSumFromCenter(
            self):  # suma odleglosci od srodka ciezkosci, jeden to kazda odleglosc podniesiona do kwadratu
        distanceSumPower = 0
        distanceSum = 0
        for p in self.domain:
            distanceSumPower += self.calculateDistance(p[0], p[1], self.centerOfMass[0], self.centerOfMass[1]) ** 2
            distanceSum += self.calculateDistance(p[0], p[1], self.centerOfMass[0], self.centerOfMass[1])
        self.distanceFromCenter = distanceSum
        self.distanceFromCenterPower = distanceSumPower

    def findMinDistSum(self):  # suma minimalna odleglosc od krawedzi
        mindist = float('inf')
        for areaPoint in self.domain:
            for edgePoint in self.edge:
                dist = self.calculateDistance(areaPoint[0], areaPoint[1], edgePoint[0][0], edgePoint[0][1]) # ? czy tutaj rzutować na int
                if dist < mindist:
                    mindist = dist
            self.minDistanceFromEgdeSum += mindist
            mindist = float('inf')

    def calculateDistance(self, x1, y1, x2, y2):
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distance

    def calculateHeightWidth(self):
        maxXdist = -1
        maxYdist = -1
        for edgePoint1 in self.edge:
            for edgePoint2 in self.edge:
                distX = self.calculateDistance(edgePoint1[0][0], 0, edgePoint2[0][0], 0)
                distY = self.calculateDistance(0, edgePoint1[0][1], 0, edgePoint2[0][1])
                if distX > maxXdist:
                    maxXdist = distX
                if distY > maxYdist:
                    maxYdist = distY
        self.LW = maxXdist
        self.LH = maxYdist

    def calculateMaxMinFromCenter(self): #najwieszka i najmniejsza odleglosc miedzy srodkiem i krawedzia
        maxdist = -1
        mindist = float('inf')
        for edgePoint in self.edge:
            dist = self.calculateDistance(edgePoint[0][0], edgePoint[0][1], self.centerOfMass[0], self.centerOfMass[1])
            if dist > maxdist:
                maxdist = dist
            if dist < mindist:
                mindist = dist
        self.maxDistaceCenterEdge = maxdist
        self.minDistaceCenterEdge = mindist

    def calculateMaxDistanceGrain(self): #najwięsza odleglość miedzy punktami ziarna
        maxdist = -1
        for areaPoint1 in self.domain:
            for areaPoint2 in self.domain:
                dist = self.calculateDistance(areaPoint1[0], areaPoint1[1], areaPoint2[0], areaPoint2[1])
                if dist > maxdist:
                    maxdist = dist
        self.maxDistancePoints = maxdist