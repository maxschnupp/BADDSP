import audio_features
import restore_model
from scipy.io.wavfile import write
import numpy as np
import ddsp
import constants

def write_audio_outputs_to_wav(target_file_name, floats):
    if len(floats.shape) == 2:
        floats = floats[0]
    normaliser = float(np.iinfo(np.int16).max)
    ints = np.array(np.asarray(floats) * normaliser, dtype=np.int16)
    write('{}/{}'.format(constants.AUDIO_OUTPUT, target_file_name),
          ddsp.spectral_ops.CREPE_SAMPLE_RATE, ints)

def transfer_timbre(source_file_name, target_file_name):
    print("transfering timbre")
    audio = audio_features.get_audio_file_as_numpy_array(source_file_name)
    af = audio_features.get_audio_features(source_file_name)
    gin_file = restore_model.get_gin_file_path()
    audio_features_trimmed = restore_model.get_trimmed_audio_features(
        gin_file, audio, af)

    ckpt = restore_model.get_chekpoint_path()
    model = restore_model.restore_model(audio_features_trimmed, ckpt)
    outputs = model(audio_features_trimmed, training=False)
    print("--- fetching audio from outputs --- ")
    audio_gen = model.get_audio_from_outputs(outputs)
    print(type(audio_gen))
    write_audio_outputs_to_wav(target_file_name, audio_gen)
    
