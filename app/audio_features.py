import note_seq
import ddsp.training
import ddsp
import constants
import numpy as np


def audio_to_numpy_array(wav_data, sample_rate=ddsp.spectral_ops.CREPE_SAMPLE_RATE, normalize_db=0.1, mono=True):
    return note_seq.audio_io.wav_data_to_samples_pydub(
        wav_data=wav_data,
        sample_rate=sample_rate,
        normalize_db=normalize_db,
        num_channels=1 if mono else None
    )


def get_audio_file_as_numpy_array(file_name):
    print('getting audio as numpy array')
    with open('{}/{}'.format(constants.AUDIO_INPUT, file_name), 'rb') as file_descriptor:
        contents = file_descriptor.read()
        audio = audio_to_numpy_array(contents)
        if len(audio.shape) == 1:
            audio=audio[np.newaxis, :]
        return audio


def get_audio_features(file_name):
    print('getting audio features')
    audio=get_audio_file_as_numpy_array(file_name)

    ddsp.spectral_ops.reset_crepe()

    audio_features=ddsp.training.metrics.compute_audio_features(audio)
    audio_features['loudness_db']=audio_features['loudness_db'].astype(np.float32)

    return audio_features
