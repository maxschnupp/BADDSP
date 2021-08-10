import preparedataset
import constants
import os


def train(audio_folder_path):
    print(audio_folder_path)

    preparedataset.prepare_dataset(audio_folder_path)
    preparedataset.save_dataset_stats_as('dataset_statistics.pkl')

    cmd_string = ("ddsp_run \ " +
    " --mode=train \ " +
    " --alsologtostderr \ " +
    " --save_dir=\"{}\" \ ".format(constants.SAVE_DIR) +
    " --gin_file=models/solo_instrument.gin \ " +
    " --gin_file=datasets/tfrecord.gin \ " +
    " --gin_param=\"TFRecordProvider.file_pattern='{}'\" \ ".format(constants.TRAIN_TFRECORD_FILEPATTERN) +
    " --gin_param=\"batch_size=16\" \ " +
    " --gin_param=\"train_util.train.num_steps=30000\" \ " +
    " --gin_param=\"train_util.train.steps_per_save=300\" \ " +
    " --gin_param=\"trainers.Trainer.checkpoints_to_keep=10\" \ ")

    print(cmd_string)

    os.system(cmd_string)
