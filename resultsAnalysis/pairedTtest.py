
import numpy as np
from scipy import stats
from typing import List, Dict
ALPHA = 0.025
#Hypothesis: transfers with opposing characterstics perform worse than those with matching ones
#   ie. (mean subjective rating of opposing transfers) - (mean subjective rating of matching transfers) < 0
# H0: transfers with opposing characterstics perform as well as or better than those with matching ones
#   ie. (mean subjective rating of opposing transfers) - (mean subjective rating of matching transfers) >= 0
# take the opposing scores - matching and check it is significantly under 0 so as to reject the null hypothesis
def pairedT(participantGroupedScores: List[Dict[str, List[int]]]):
    populationMean = 0
    n = len(participantGroupedScores)
    values = []
    for item in participantGroupedScores: 
        values.append([np.mean(item['matchingScores']), np.mean(item['opposingScores'])])
    differences = []
    for item in values:
        differences.append(item[1] - item[0])
    sampleMeanDifference = np.mean(differences)
    standardDeviation = np.std(differences)
    calculatedT = (sampleMeanDifference - populationMean) / (standardDeviation / np.sqrt(n))
    degreesOfFreedom = n - 1
    criticalT = stats.t.ppf(ALPHA, degreesOfFreedom)
    confidence = criticalT * (standardDeviation / np.sqrt(n))
    print('sample mean', sampleMeanDifference)
    print('standard deviation', standardDeviation)
    print('t_c', calculatedT)
    print('critical t', criticalT)
    print('t_c < critical t', calculatedT < criticalT)
    print('confidence interval {} +/- {}'.format(sampleMeanDifference, confidence))
    

