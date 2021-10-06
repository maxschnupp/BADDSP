import audio_features
import unittest
import numpy as np
AUDIO_FILE = 'test_audio.wav'

class TestAudioFeatures(unittest.TestCase):

    def test_get_audio_file_as_numpy_array(self):
        audio_array = audio_features.get_audio_file_as_numpy_array(AUDIO_FILE)
        print(type(audio_array))
        self.assertIsInstance(audio_array, np.ndarray)

    def test_get_audio_features(self):
        result = audio_features.get_audio_features(AUDIO_FILE)
        print(str(result.keys()))
        self.assertSetEqual(set(result.keys()), set(['audio', 'loudness_db', 'f0_hz', 'f0_confidence']))