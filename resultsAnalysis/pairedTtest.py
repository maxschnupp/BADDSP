import numpy as np
from scipy import stats
#participantGroupedScores[0] should represent matching scores [1] unmatching
def pairedT(participantGroupedScores, alpha):
    populationMean = 0
    n = len(participantGroupedScores)
    values = []
    for item in participantGroupedScores: 
        values.append([np.mean(item[0]), np.mean(item[1])])
    differences = []
    for item in values:
        differences.append(item[1] - item[0])
    sampleMean = np.mean(differences)
    standardDeviation = np.std(differences)
    criticalT = (sampleMean - populationMean) / (standardDeviation / np.sqrt(n))
    degreesOfFreedom = n - 1


