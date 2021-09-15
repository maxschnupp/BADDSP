import unittest
import preparedataset
import os
import constants
import testutils

class TestPrepareDataset(unittest.TestCase):
    def test_preparedataset(self):
        folderPath = "testAudio"
        res = preparedataset.prepare_dataset(folderPath)
        # it makes the correct terminal call
        self.assertTrue(res == "ddsp_prepare_tfrecord --input_audio_filepatterns=./assets/testAudio/*"
            + " --output_tfrecord_path=" + constants.TRAIN_TFRECORD +
            " --num_shards=10 --alsologtostderr")
        # the terminal call results in file creation
        self.assertTrue(testutils.file_in_folder_matches_regex('./assets/data', '^train.tfrecord'))


    def test_save_dataset_stats_as(self):
        filename = 'dataset_statistics_test.pkl'
        preparedataset.save_dataset_stats_as(filename)
        # check for file creation
        self.assertTrue(os.path.exists(os.path.join(constants.STATS_PATH, filename)))
