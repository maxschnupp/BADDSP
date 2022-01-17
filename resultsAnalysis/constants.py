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

NAME_LOOKUP_TABLE = {
    COLUMN_NAMES[0]: 'Slide Guitar to Slide Guitar',  
    COLUMN_NAMES[1]: 'Slide Guitar to Vibraphone',  
    COLUMN_NAMES[2]: 'Slide Guitar to Viola',  
    COLUMN_NAMES[3]: 'Slide Guitar to FlugelHorn',  
    COLUMN_NAMES[4]: 'Vibraphone to Vibraphone',  
    COLUMN_NAMES[5]: 'Vibraphone to Slide Guitar',  
    COLUMN_NAMES[6]: 'Vibraphone to Viola',  
    COLUMN_NAMES[7]: 'Vibraphone to FlugelHorn',  
    COLUMN_NAMES[8]: 'Viola to Slide Guitar',  
    COLUMN_NAMES[9]: 'Viola to Vibraphone', 
    COLUMN_NAMES[10]: 'Viola to Viola',  
    COLUMN_NAMES[11]: 'Viola to Flugelhorn',  
    COLUMN_NAMES[12]: 'Flugel Horn to Slide Guitar',  
    COLUMN_NAMES[13]: 'Flugel Horn to Vibraphone',  
    COLUMN_NAMES[14]: 'Flugel Horn to Viola',  
    COLUMN_NAMES[15]: 'Flugel Horn to FlugelHorn'
}

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

SCORES_DICT_TEMPLATE = {
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