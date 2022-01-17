import csv
import numpy as np
import copy
from typing import List, Dict
from constants import NAME_LOOKUP_TABLE, COLUMN_NAMES, MATCH_LOOKUP_TABLE, SCORES_DICT_TEMPLATE



def convertStringToNumericScore(label: str):
    if(label == 'AO01') : return 1
    if(label == 'AO02') : return 6
    if(label == 'AO03') : return 5
    if(label == 'AO04') : return 4
    if(label == 'AO05') : return 3
    if(label == 'AO06') : return 2
    else: raise ValueError('invalid score label {}!'.format(label))


def convertAllStringsToNumericScores(labels):
    newList = []
    for item in labels:
        newList.append(convertStringToNumericScore(item))
    return newList

def getParticipantQsAndAs(filepath: str) -> List[List[Dict]]:
    participantQsAndAs = []
    with open(filepath, 'r') as survey_data_raw:
        csv_reader = csv.DictReader(survey_data_raw)
        #for each survey entry
        for row in csv_reader:
            new_entry = []
            # if the survey was submitted ie. the data is complete
            if(row['submitdate'] != ''):
                #for every question
                for key in COLUMN_NAMES:
                    # add the question label along with the score converted to numeric
                    new_entry.append({'label': key, 'value': convertStringToNumericScore(row[key])})
                #add the new entry to the dataset
                participantQsAndAs.append(new_entry)
    return participantQsAndAs

def getParticipantScoresGroupedByCharMatch(charMatch: str, filepath: str) -> List[Dict]:
    participantsScores = []
    participantQsAndAs = getParticipantQsAndAs(filepath)
    for response in participantQsAndAs:
        newEntry = {'matchingScores': [], 'opposingScores': []}
        # for each answer
        for labelValuePair in response:
            matchingAccordingToChar = MATCH_LOOKUP_TABLE[labelValuePair["label"]][charMatch]
            if matchingAccordingToChar:
                newEntry['matchingScores'].append(labelValuePair['value'])
            else:
                newEntry['opposingScores'].append(labelValuePair['value'])
        participantsScores.append(newEntry)
    return participantsScores

def getQuestionScoresAsDict(filepath: str):
    
    scoresDict = copy.deepcopy(SCORES_DICT_TEMPLATE)

    with open(filepath, 'r') as survey_data_raw:
        csv_reader = csv.DictReader(survey_data_raw)
    
        for row in csv_reader:
            for key in COLUMN_NAMES:
                #discard data from incomplete surveys
                if(row['submitdate'] != '') : scoresDict[key]['values'].append(row[key])
        
    for key in scoresDict.keys():
        scoresDict[key]['values'] = convertAllStringsToNumericScores(scoresDict[key]['values'])

    return scoresDict
    

def getMeanScoresGroupedBy(characteristicMatch: str, filepath: str):
    returnValue = {'matching': [], 'opposing': []}
    scores = getQuestionScoresAsDict(filepath)
    for key in scores.keys():
        item = scores[key]
        if item[characteristicMatch]:
            returnValue['matching'].append(np.mean(item['values']))
        else:
            returnValue['opposing'].append(np.mean(item['values']))
    return returnValue

def getMeansForEachResynthesisExampleInDfFormat(filepath: str):
    returnValue = {'Model': [], 'Mean Score': []}
    scores = getQuestionScoresAsDict(filepath)
    resynthesisExamples = {
        'sli2sli[SQ001]': {'name' : 'Slide Guitar'}, 
        'vib2vib[SQ001]': {'name' : 'Vibraphone'},
        'flu2flu[SQ001]': {'name' : 'Flugel Horn'},
        'vio2vio[SQ001]': {'name' : 'Viola'},
    }
    for key in resynthesisExamples.keys():
        returnValue['Model'].append(resynthesisExamples[key]['name'])
        returnValue['Mean Score'].append(np.mean(scores[key]['values']))
    return returnValue

def getMeansForEachExampleInDfFormat(filepath: str):
    returnValue = {'Model': [], 'Mean Score': []}
    scores = getQuestionScoresAsDict(filepath)
    for key in scores.keys():
        returnValue['Model'].append(key[0:7])
        returnValue['Mean Score'].append(np.mean(scores[key]['values']))
    return returnValue