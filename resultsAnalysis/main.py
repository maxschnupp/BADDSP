import csvInterface
import pairedTtest
import plots
FILEPATH = 'data/test.csv'

print("paired t test for matching excitations")

participantScoresGroupedByExcitationMatch = csvInterface.getParticipantScoresGroupedByCharMatch('excitationMatch', FILEPATH)
pairedTtest.pairedT(participantScoresGroupedByExcitationMatch)

print("paired t test for matching pitch resolutions")

participantScoresGroupedByPitchResMatch = csvInterface.getParticipantScoresGroupedByCharMatch('pitchResMatch', FILEPATH)
pairedTtest.pairedT(participantScoresGroupedByPitchResMatch)

plots.boxplotGroupedMeans(FILEPATH)

plots.barplotResynthesisMeans(FILEPATH)

plots.barplotAllMeans(FILEPATH)