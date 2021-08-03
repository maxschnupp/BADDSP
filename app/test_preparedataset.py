import preparedataset
import os
# just running it for now
# TODO: find out what valid pattern looks like for target folder


def test_preparedataset():
    folderPath = "testAudio"
    res = preparedataset.prepareDataset(folderPath)
    assert(res == "ddsp_prepare_tfrecord --input_audio_filepatterns=./assets/testAudio/*"
           + " --output_tfrecord_path=./assets/data/train.tfrecord --num_shards=10 --alsologtostderr")
    assert(os.path.exists("./assets/data"))
