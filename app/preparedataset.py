import os
import glob

TRAIN_TFRECORD = './assets/data/train.tfrecord'
TRAIN_TFRECORD_FILEPATTERN = TRAIN_TFRECORD + '*'


def replaceWhitespaceWithUnderscoreInFilenames(folderPath):
    for fname in os.listdir(folderPath):
        os.rename(os.path.join(folderPath, fname),
                  os.path.join(folderPath, os.path.basename(fname).replace(' ', '_')))


def prepareDataset(audioFolderPath):

    audio_files = os.path.join("./assets/", audioFolderPath)

    audioFilePattern = audio_files + '/*'

    # format audiofile names

    replaceWhitespaceWithUnderscoreInFilenames(audio_files)

    dataset_files = glob.glob('./assets/data' + '/*')

    print("here")

    # if dataset already populated break
    if len(dataset_files) > 0:
        return

    else:
        # make new dataset
        print("audioFilePattern " + audioFilePattern)
        if not glob.glob(audioFilePattern):
            raise ValueError('No audio files found.')

        os.system("ls")
        # use the ddsp helper to prepare tfrecord from audio

        cmdString = ("ddsp_prepare_tfrecord" +
                     " --input_audio_filepatterns=" + audioFilePattern +
                     " --output_tfrecord_path=" + TRAIN_TFRECORD +
                     " --num_shards=10"
                     " --alsologtostderr")

        os.system(cmdString)
        #for testing purposes only
        return cmdString
