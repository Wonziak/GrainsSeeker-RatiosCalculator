import matplotlib.pyplot as plt
from collections import Counter
import grain_class

filename = 'results.txt'
malinowska = []
blair_bliss = []
danielsson = []
haralick = []
mz = []
rls = []
rf = []
rc1 = []
rc2 = []
rcom = []
lp1 = []
lp2 = []
lp3 = []
allRatios = []

malinowskaHist = 0
blair_blissHist = 0
danielssonHist = 0
haralickHist = 0
mzHist = 0
rlsHist = 0
rfHist = 0
rc1Hist = 0
rc2Hist = 0
rcomHist = 0
lp1Hist = 0
lp2Hist = 0
lp3Hist = 0

allHistograms = [malinowskaHist,
                 blair_blissHist,
                 danielssonHist,
                 haralickHist,
                 mzHist,
                 rlsHist,
                 rfHist,
                 rc1Hist,
                 rc2Hist,
                 rcomHist,
                 lp1Hist,
                 lp2Hist,
                 lp3Hist]
names = ['Malinowska',
        'Blair Bliss',
        'Danielsson',
        'Haralick',
        'Mz',
        'RLS',
        'RF',
        'RC1',
        'RC2',
        'RCOM',
        'LP1',
        'LP2',
        'LP3']


def createSeriesFromRatios(grains):
    for Grain in grains:
        malinowska.append(Grain.Malinowska)
        blair_bliss.append(Grain.Blair_Bliss)
        danielsson.append(Grain.Danielsson)
        haralick.append(Grain.Haralick)
        rls.append(Grain.RLS)
        rf.append(Grain.RF)
        rc1.append(Grain.RC1)
        rc2.append(Grain.RC2)
        rcom.append(Grain.RCom)
        lp1.append(Grain.Lp1)
        lp2.append(Grain.Lp2)
        lp3.append(Grain.Lp3)
        mz.append(Grain.Mz)
    allRatios.append(malinowska)
    allRatios.append(blair_bliss)
    allRatios.append(danielsson)
    allRatios.append(haralick)
    allRatios.append(mz)
    allRatios.append(rls)
    allRatios.append(rf)
    allRatios.append(rc1)
    allRatios.append(rc2)
    allRatios.append(rcom)
    allRatios.append(lp1)
    allRatios.append(lp2)
    allRatios.append(lp3)


def createHistograms(grainscount):

    for i in range(len(allRatios)):
        allHistograms[i] = Counter(allRatios[i])
        for key in allHistograms[i]:
            allHistograms[i][key] = allHistograms[i][key]/grainscount

        plt.bar(range(len(allHistograms[i])), allHistograms[i].values(), width=0.15, color='g')  #rysowanie wykresów histogramów
        plt.xticks(range(len(allHistograms[i])), allHistograms[i].keys(), rotation=90)
        plt.title(names[i])
        plt.show()

    results = open(filename, 'w')
    for i in range(len(allHistograms)):
        results.write(names[i]+':  '+str(allHistograms[i])[9:len(str(allHistograms[i]))-2]+'\n')
    results.close()
