import constants
import os
import gin
import tensorflow as tf
import ddsp

def get_file_name_containing_string(search_string, directory):
    for _ , _ , files in os.walk(directory):
        for file in files:
            if search_string in file:
                return file

def get_gin_file_path():
    print("getting gin file path")
    search_string = '.gin'
    gin_file_name = get_file_name_containing_string(search_string, constants.SAVE_DIR)
    try:
        gin_file = os.path.join(constants.SAVE_DIR, gin_file_name)
        return gin_file
    except:
        print("Could not load gin file!")

def get_chekpoint_path():
    print("getting checkpoint")
    try:
        checkpoint_files = [f for f in tf.io.gfile.listdir(constants.SAVE_DIR) if 'ckpt' in f]
        checkpoint_name = checkpoint_files[0].split('.')[0]
        return os.path.join(constants.SAVE_DIR, checkpoint_name)
    except:
        print("could not locate checkpoint")

def restore_model(audio_features, ckpt):
    print("restoring model, checkpoint:", ckpt)
    model = ddsp.training.models.Autoencoder()
    print('got here1')
    ## supress compiler warnings on missing variables as not training
    model.restore(ckpt, verbose=False)
    print('got here2')
    _ = model(audio_features, training=False)
    print("done")
    return model

def get_trimmed_audio_features(gin_file, audio, audio_features):
    print("getting trimmed audio features", gin_file)
    with gin.unlock_config():
        gin.parse_config_file(gin_file, skip_unknown=True)
    
    time_steps_train = gin.query_parameter('F0LoudnessPreprocessor.time_steps')
    n_samples_train = gin.query_parameter('Harmonic.n_samples')
    hop_size = int(n_samples_train / time_steps_train)

    time_steps = int(audio.shape[1] / hop_size)
    n_samples = time_steps * hop_size

    gin_params = [
        'Harmonic.n_samples = {}'.format(n_samples),
        'FilteredNoise.n_samples = {}'.format(n_samples),
        'F0LoudnessPreprocessor.time_steps = {}'.format(time_steps),
        'oscillator_bank.use_angular_cumsum = True',
    ]   

    with gin.unlock_config():
        gin.parse_config(gin_params)
    
    for key in ['f0_hz', 'f0_confidence', 'loudness_db']:
        audio_features[key] = audio_features[key][:time_steps]
        audio_features['audio'] = audio_features['audio'][:, :n_samples]
    
    return audio_features