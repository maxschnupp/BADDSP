import audio_features
import restore_model
from scipy.io.wavfile import write
import ddsp

def transfer_timbre(source_file_name, target_path):
    print("transfering timbre")
    audio = audio_features.get_audio_file_as_numpy_array(source_file_name)
    af = audio_features.get_audio_features(source_file_name)
    gin_file = restore_model.get_gin_file_path()
    audio_features_trimmed = restore_model.get_trimmed_audio_features(gin_file, audio, af)

    ckpt = restore_model.get_chekpoint_path()
    model = restore_model.restore_model(audio_features_trimmed, ckpt)
    outputs = model(audio_features_trimmed, training=False)

    audio_gen = model.get_audio_from_outputs(outputs)
    write(target_path, ddsp.spectral_ops.CREPE_SAMPLE_RATE, audio_gen)


