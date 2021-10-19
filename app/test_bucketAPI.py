import bucketAPI
import unittest
import unittest.mock as mock
class TestBucketAPI(unittest.TestCase):
    def test_upload_to_gin_bucket(self):
            bucketAPI.upload_to_gin_bucket("vibraphone-ckpt-1800.data-00000-of-00001", "testing")

    def test_upload_to_audio_bucket(self):
            bucketAPI.upload_to_audio_bucket("test_audio.wav", "testing")