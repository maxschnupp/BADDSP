import csv
import numpy as np
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

def getParticipantQsAndAs(filepath: str):
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



def getQuestionScoresAsDict(filepath: str):
    
    scoresDict = {
        'sli2sli[SQ001]': {'values' : [], 'excitationMatch': True, 'pitchResMatch': True},  
        'sli2vib[SQ001]': {'values' : [], 'excitationMatch': True, 'pitchResMatch': False},  
        'sli2vio[SQ001]': {'values' : [], 'excitationMatch': False, 'pitchResMatch': True},  
        'sli2flu[SQ001]': {'values' : [], 'excitationMatch': False, 'pitchResMatch': False},  
        'vib2vib[SQ001]': {'values' : [], 'excitationMatch': True, 'pitchResMatch': True},  
        'vib2sli[SQ001]': {'values' : [], 'excitationMatch': True, 'pitchResMatch': False},  
        'vib2vio[SQ001]': {'values' : [], 'excitationMatch': False, 'pitchResMatch': False},  
        'vib2flu[SQ001]': {'values' : [], 'excitationMatch': False, 'pitchResMatch': True},  
        'vio2sli[SQ001]': {'values' : [], 'excitationMatch': False, 'pitchResMatch': True},  
        'vio2vib[SQ001]': {'values' : [], 'excitationMatch': False, 'pitchResMatch': False},  
        'vio2vio[SQ001]': {'values' : [], 'excitationMatch': True, 'pitchResMatch': True},  
        'vio2flu[SQ001]': {'values' : [], 'excitationMatch': True, 'pitchResMatch': False},  
        'flu2sli[SQ001]': {'values' : [], 'excitationMatch': False, 'pitchResMatch': False},  
        'flu2vib[SQ001]': {'values' : [], 'excitationMatch': False, 'pitchResMatch': True},  
        'flu2vio[SQ001]': {'values' : [], 'excitationMatch': True, 'pitchResMatch': False},  
        'flu2flu[SQ001]': {'values' : [], 'excitationMatch': True , 'pitchResMatch': True}
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