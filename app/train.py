import preparedataset
import constants
import os
import gin_file_watcher


def train(audio_folder_name):
    print(audio_folder_name)

    ## start file watcher thread to autosave checkpoints to bucket
    file_thread = gin_file_watcher.get_watchdog_thread()
    file_thread.start()

    preparedataset.prepare_dataset(audio_folder_name)
    preparedataset.save_dataset_stats_as('dataset_statistics.pkl')

    cmd_string = ("ddsp_run \ " +
    " --mode=train \ " +
    " --alsologtostderr \ " +
    " --save_dir=\"{}\" \ ".format(constants.SAVE_DIR) +
    " --gin_file=models/solo_instrument.gin \ " +
    " --gin_file=datasets/tfrecord.gin \ " +
    " --gin_param=\"TFRecordProvider.file_pattern='{}'\" \ ".format(constants.TRAIN_TFRECORD_FILEPATTERN) +
    ##batch size should be 16 reducing to 1 to see if ram is killing training
    " --gin_param=\"batch_size=1\" \ " +
    " --gin_param=\"train_util.train.num_steps=30000\" \ " +
    " --gin_param=\"train_util.train.steps_per_save=300\" \ " +
    " --gin_param=\"trainers.Trainer.checkpoints_to_keep=10\" \ ")

    print(cmd_string)

    os.system(cmd_string)
