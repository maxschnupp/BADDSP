import csv
import numpy as np
from typing import List, Dict

COLUMN_NAMES = [
    'sli2sli[SQ001]',
    'sli2vib[SQ001]',
    'sli2vio[SQ001]',
    'sli2flu[SQ001]',
    'vib2vib[SQ001]',
    'vib2sli[SQ001]',
    'vib2vio[SQ001]',
    'vib2flu[SQ001]',
    'vio2sli[SQ001]',
    'vio2vib[SQ001]',
    'vio2vio[SQ001]',
    'vio2flu[SQ001]',
    'flu2sli[SQ001]',
    'flu2vib[SQ001]',
    'flu2vio[SQ001]',
    'flu2flu[SQ001]'
]

MATCH_LOOKUP_TABLE = {
    COLUMN_NAMES[0]: { 'excitationMatch': True, 'pitchResMatch': True},  
    COLUMN_NAMES[1]: { 'excitationMatch': True, 'pitchResMatch': False},  
    COLUMN_NAMES[2]: { 'excitationMatch': False, 'pitchResMatch': True},  
    COLUMN_NAMES[3]: { 'excitationMatch': False, 'pitchResMatch': False},  
    COLUMN_NAMES[4]: { 'excitationMatch': True, 'pitchResMatch': True},  
    COLUMN_NAMES[5]: { 'excitationMatch': True, 'pitchResMatch': False},  
    COLUMN_NAMES[6]: { 'excitationMatch': False, 'pitchResMatch': False},  
    COLUMN_NAMES[7]: { 'excitationMatch': False, 'pitchResMatch': True},  
    COLUMN_NAMES[8]: { 'excitationMatch': False, 'pitchResMatch': True},  
    COLUMN_NAMES[9]: { 'excitationMatch': False, 'pitchResMatch': False},  
    COLUMN_NAMES[10]: { 'excitationMatch': True, 'pitchResMatch': True},  
    COLUMN_NAMES[11]: { 'excitationMatch': True, 'pitchResMatch': False},  
    COLUMN_NAMES[12]: { 'excitationMatch': False, 'pitchResMatch': False},  
    COLUMN_NAMES[13]: { 'excitationMatch': False, 'pitchResMatch': True},  
    COLUMN_NAMES[14]: { 'excitationMatch': True, 'pitchResMatch': False},  
    COLUMN_NAMES[15]: { 'excitationMatch': True , 'pitchResMatch': True}
}

def convertStringToNumericScore(label: str):
    if(label == 'AO01') : return 1
    if(label == 'AO02') : return 6
    if(label == 'AO03') : return 5
    if(label == 'AO04') : return 4
    if(label == 'AO05') : return 3
    if(label == 'AO06') : return 2
    else: raise ValueError('invalid score label!')


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
    
    scoresDict = {
        COLUMN_NAMES[0]: {'values' : [], **MATCH_LOOKUP_TABLE[COLUMN_NAMES[0]]},  
        COLUMN_NAMES[1]: {'values' : [], **MATCH_LOOKUP_TABLE[COLUMN_NAMES[1]]},  
        COLUMN_NAMES[2]: {'values' : [], **MATCH_LOOKUP_TABLE[COLUMN_NAMES[2]]},  
        COLUMN_NAMES[3]: {'values' : [], **MATCH_LOOKUP_TABLE[COLUMN_NAMES[3]]},  
        COLUMN_NAMES[4]: {'values' : [], **MATCH_LOOKUP_TABLE[COLUMN_NAMES[4]]},  
        COLUMN_NAMES[5]: {'values' : [], **MATCH_LOOKUP_TABLE[COLUMN_NAMES[5]]},   
        COLUMN_NAMES[6]: {'values' : [], **MATCH_LOOKUP_TABLE[COLUMN_NAMES[6]]},  
        COLUMN_NAMES[7]: {'values' : [], **MATCH_LOOKUP_TABLE[COLUMN_NAMES[7]]},  
        COLUMN_NAMES[8]: {'values' : [], **MATCH_LOOKUP_TABLE[COLUMN_NAMES[8]]},  
        COLUMN_NAMES[9]: {'values' : [], **MATCH_LOOKUP_TABLE[COLUMN_NAMES[9]]},  
        COLUMN_NAMES[10]: {'values' : [], **MATCH_LOOKUP_TABLE[COLUMN_NAMES[10]]},  
        COLUMN_NAMES[11]: {'values' : [], **MATCH_LOOKUP_TABLE[COLUMN_NAMES[11]]},  
        COLUMN_NAMES[12]: {'values' : [], **MATCH_LOOKUP_TABLE[COLUMN_NAMES[12]]},  
        COLUMN_NAMES[13]: {'values' : [], **MATCH_LOOKUP_TABLE[COLUMN_NAMES[13]]},  
        COLUMN_NAMES[14]: {'values' : [], **MATCH_LOOKUP_TABLE[COLUMN_NAMES[14]]},  
        COLUMN_NAMES[15]: {'values' : [], **MATCH_LOOKUP_TABLE[COLUMN_NAMES[15]]}
    }

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