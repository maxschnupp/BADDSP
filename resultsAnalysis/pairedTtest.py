import numpy as np
from scipy import stats
ALPHA = 0.05
#participantGroupedScores[0] should represent matching scores [1] opposite
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
    calculatedT = (sampleMean - populationMean) / (standardDeviation / np.sqrt(n))
    degreesOfFreedom = n - 1
    criticalT = stats.t.ppf(ALPHA, degreesOfFreedom, sampleMean, standardDeviation)

    print('t_c', calculatedT)
    print('critical t', criticalT)
    print('t_c < critical t', criticalT)
    

