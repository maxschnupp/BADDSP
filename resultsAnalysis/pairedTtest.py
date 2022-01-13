from xmlrpc.client import boolean
import numpy as np
from scipy import stats
from typing import List, Dict
ALPHA = 0.025
#participantGroupedScores[0] should represent matching scores [1] opposite
def pairedT(participantGroupedScores: List[Dict[str, List[int]]]):
    populationMean = 0
    n = len(participantGroupedScores)
    values = []
    for item in participantGroupedScores: 
        values.append([np.mean(item['matchingScores']), np.mean(item['opposingScores'])])
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
    print('t_c < critical t', calculatedT < criticalT)
    

