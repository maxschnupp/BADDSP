import os
import glob
import ddsp
import ddsp.training
import tensorflow as tf
import pickle
import constants


def replace_whitespace_with_underscore_in_filenames(folder_path):
    for fname in os.listdir(folder_path):
        os.rename(os.path.join(folder_path, fname),
                  os.path.join(folder_path, os.path.basename(fname).replace(' ', '_')))


def prepare_dataset(audio_folder_path):

    audio_files = os.path.join("./assets/", audio_folder_path)

    audio_file_pattern = audio_files + '/*'

    # format audiofile names

    replace_whitespace_with_underscore_in_filenames(audio_files)

    dataset_files = glob.glob('./assets/data' + '/*')

    # if dataset already populated break
    if len(dataset_files) > 0:
        return

    else:
        # make new dataset
        print("audio_file_pattern " + audio_file_pattern)
        if not glob.glob(audio_file_pattern):
            raise ValueError('No audio files found.')

        # use the ddsp helper to prepare tfrecord from audio

        cmd_string = ("ddsp_prepare_tfrecord" +
                     " --input_audio_filepatterns=" + audio_file_pattern +
                     " --output_tfrecord_path=" + constants.TRAIN_TFRECORD +
                     " --num_shards=10"
                     " --alsologtostderr")

        os.system(cmd_string)
        # for testing purposes only
        return cmd_string


def save_dataset_stats_as(filename, batch_size=1, power_frame_size=256):
    data_provider = ddsp.training.data.TFRecordProvider(
        constants.TRAIN_TFRECORD_FILEPATTERN)

    file_path = os.path.join(constants.STATS_PATH, filename)

    os.system('mkdir -p ' + constants.STATS_PATH)

    ds_stats = ddsp.training.postprocessing.compute_dataset_statistics(
        data_provider, batch_size, power_frame_size)

    if file_path is not None:
        with tf.io.gfile.GFile(file_path, 'wb') as f:
            pickle.dump(ds_stats, f)
        

    print(f'Done! Saved dataset statistics to: {file_path}')

    return ds_stats
