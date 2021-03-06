import unittest
import csvInterface
FILEPATH = 'data/test.csv'

def printDictionaryReadable(dictionary : dict):
    for key in dictionary.keys():
        print(key, dictionary[key])

class TestCSVInterface(unittest.TestCase):
        def test_getScoresAsDict(self):
            scoresDict = csvInterface.getQuestionScoresAsDict(FILEPATH)
            printDictionaryReadable(scoresDict)
            scoresDict = csvInterface.getQuestionScoresAsDict(FILEPATH)
        
        
        # def test_getMeanScoresGroupedBy(self):
        #     print('group by excitation')
        #     returnByExcitation = csvInterface.getMeanScoresGroupedBy('excitationMatch', FILEPATH)
        #     printDictionaryReadable(returnByExcitation)
        #     print('group by pitch resolution')
        #     returnByPitchRes = csvInterface.getMeanScoresGroupedBy('pitchResMatch', FILEPATH)
        #     printDictionaryReadable(returnByPitchRes)

        # def test_getParticipantQsAndAs(self):
        #     returnValue = csvInterface.getParticipantQsAndAs(FILEPATH)
        #     for item in returnValue: print(item)

        # def test_getParticipantScoresGroupedByCharMatch(self):
        #     print('group by excitation')
        #     returnByExcitation = csvInterface.getParticipantScoresGroupedByCharMatch('excitationMatch', FILEPATH)
        #     print(returnByExcitation)
        #     print('group by pitch resolution')
        #     returnByPitchRes = csvInterface.getParticipantScoresGroupedByCharMatch('pitchResMatch', FILEPATH)
        #     print(returnByPitchRes)

