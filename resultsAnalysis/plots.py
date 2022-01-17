
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from csvInterface import getMeanScoresGroupedBy, getMeansForEachResynthesisExampleInDfFormat, getMeansForEachExampleInDfFormat
import seaborn

def stripPlot(data, label):
    seaborn.set(style = 'whitegrid')
    dataset = pd.DataFrame({label : data})
    seaborn.stripplot(x=label, data=dataset)
    plt.show()

def groupedBoxplot(matching, opposing, label):
    scores = []
    char_match = []
    for item in matching:
        scores.append(item)
        char_match.append('Matching')
    for item in opposing:
        scores.append(item)
        char_match.append('Opposing')
    dataFrame = pd.DataFrame({'Mean Scores' : scores, label: char_match})
    boxplot = dataFrame.boxplot(column=['Mean Scores'], by=label, grid=False)
    boxplot.get_figure().suptitle('')
    boxplot.get_figure().gca().set_title("")
    boxplot.get_figure().gca().set_ylabel('mean scores')
    boxplot.plot()
    plt.title('Mean Question Scores For Matching vs Opposing {}'.format(label))
    plt.show()

def boxplotGroupedMeans(filepath):

    excitationScores = getMeanScoresGroupedBy('excitationMatch', filepath)
    pitchResScores = getMeanScoresGroupedBy('pitchResMatch', filepath)

    matchedExcitationMeans = excitationScores['matching']
    opposingExcitationMeans = excitationScores['opposing']
    groupedBoxplot(matching=matchedExcitationMeans, opposing=opposingExcitationMeans, label='Excitations')

    matchedPitchResMeans = pitchResScores['matching']
    opposingPitchResMeans = pitchResScores['opposing']
    groupedBoxplot(matching=matchedPitchResMeans, opposing=opposingPitchResMeans, label='Pitch Resolutions')

def barplotResynthesisMeans(filepath):
    data = getMeansForEachResynthesisExampleInDfFormat(filepath)
    dataFrame = pd.DataFrame(data)
    print(data)
    axis = dataFrame.plot.bar(x='Model', y='Mean Score', rot=0)
    axis.plot()
    for i, value in enumerate(data['Mean Score']):
        axis.text(i - 0.125, 0.25, str(np.round(value, 2)), color='white', fontweight='bold', fontsize=12)
    plt.title('Mean Subjective Similarity Scores for Resynthesis Examples')
    plt.show()

def barplotAllMeans(filepath):
    data = getMeansForEachExampleInDfFormat(filepath)
    dataFrame = pd.DataFrame(data)
    dfSorted = dataFrame.sort_values('Mean Score')
    print(data)
    axis = dfSorted.plot.barh(x='Model', y='Mean Score', rot=45)
    axis.plot()
    for i, value in enumerate(sorted(data['Mean Score'])):
        axis.text(0.25, i - 0.2, str(np.round(value, 2)), color='white', fontweight='bold', fontsize=8.5)
    plt.xticks(fontsize=6)
    plt.title('Mean Subjective Similarity Scores for Transfers')
    plt.show()
