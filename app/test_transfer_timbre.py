import unittest
import transfer_timbre

class TestTransferTimbre(unittest.TestCase):
    def test_transfer_timbre(self):
        transfer_timbre.transfer_timbre('test_audio.wav', 'test_out.wav')