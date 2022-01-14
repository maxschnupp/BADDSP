import pandas as pd
import matplotlib.pyplot as plt
from csvInterface import getMeanScoresGroupedBy

# def sideBySideBoxplot(matching, opposing):
#     dataFrame = pd.DataFrame({'Matching': matching, 'Opposing': opposing})
#     boxplotmatching = dataFrame.boxplot(column='Matching')
#     boxplotmatching.plot()
#     boxplotmatching = dataFrame.boxplot(column='Opposing')
#     boxplotmatching.plot()
#     plt.show()

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
    plt.title('Mean Question Scores For Matching & Opposing {}'.format(label))
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

