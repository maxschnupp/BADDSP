import unittest
import unittest.mock as mock
import transfer_timbre

class TestTransferTimbre(unittest.TestCase):

    def test_transfer_all(self):
        with mock.patch('transfer_timbre.transfer_timbre') as mock_transfer:
            transfer_timbre.transfer_all('some_label', './assets/testAudio')
            self.assertTrue(mock_transfer.called)
            mock_transfer.assert_any_call('test_audio.wav', '0-test_audio.wav', 'some_label')
            mock_transfer.assert_any_call('test_audio1.wav', '1-test_audio1.wav', 'some_label')

    # def test_transfer_timbre(self):
    #     transfer_timbre.transfer_timbre('test_audio.wav', 'test_out.wav', 'testing')