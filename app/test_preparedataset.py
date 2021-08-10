import preparedataset
import os
import constants
import testutils


def test_preparedataset():
    folderPath = "testAudio"
    res = preparedataset.prepare_dataset(folderPath)
    # it makes the correct terminal call
    assert(res == "ddsp_prepare_tfrecord --input_audio_filepatterns=./assets/testAudio/*"
           + " --output_tfrecord_path=" + constants.TRAIN_TFRECORD +
           " --num_shards=10 --alsologtostderr")
    # the terminal call results in file creation
    assert(testutils.file_in_folder_matches_regex('./assets/data', '^train.tfrecord'))


def test_save_dataset_stats_as():
    filename = 'dataset_statistics_test.pkl'
    preparedataset.save_dataset_stats_as(filename)
    # check for file creation
    assert(os.path.exists(os.path.join(constants.STATS_PATH, filename)))
