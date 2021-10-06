import restore_model
import unittest
import audio_features
import numpy as np


class TestRestoreModel(unittest.TestCase):
    def test_get_file_name_containing_string(self):
        res = restore_model.get_file_name_containing_string(
            'test', './assets/models/ddsp-solo-instrument')
        self.assertEqual(res, 'test.txt')

    def test_get_trimmed_audio_features(self):
        gin_file = restore_model.get_gin_file_path()
        trimmed_audio_features = restore_model.get_trimmed_audio_features(
            gin_file, 
            audio_features.get_audio_file_as_numpy_array('test_audio.wav'), 
            audio_features.get_audio_features('test_audio.wav')
        )   
        self.assertSetEqual(set(trimmed_audio_features.keys()), set(['audio', 'loudness_db', 'f0_hz', 'f0_confidence']))

    
    def test_restore_model(self):
        gin_file = restore_model.get_gin_file_path()
        checkpoint_path = restore_model.get_chekpoint_path()
        trimmed_audio_features = restore_model.get_trimmed_audio_features(
            gin_file, 
            audio_features.get_audio_file_as_numpy_array('test_audio.wav'), 
            audio_features.get_audio_features('test_audio.wav')
        )
        restore_model.restore_model(trimmed_audio_features, checkpoint_path)
