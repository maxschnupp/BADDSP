import csvInterface
import pairedTtest
import boxplotGroupedMeans
FILEPATH = 'data/test.csv'

print("paired t test for matching excitations")

participantScoresGroupedByExcitationMatch = csvInterface.getParticipantScoresGroupedByCharMatch('excitationMatch', FILEPATH)
pairedTtest.pairedT(participantScoresGroupedByExcitationMatch)

print("paired t test for matching pitch resolutions")

participantScoresGroupedByPitchResMatch = csvInterface.getParticipantScoresGroupedByCharMatch('pitchResMatch', FILEPATH)
pairedTtest.pairedT(participantScoresGroupedByPitchResMatch)

boxplotGroupedMeans.boxplotGroupedMeans(FILEPATH)
