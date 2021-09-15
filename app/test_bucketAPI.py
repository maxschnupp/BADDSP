import bucketAPI
import unittest
import unittest.mock as mock
class TestBucketAPI(unittest.TestCase):
    def test_upload_to_bucket(self):
            bucketAPI.upload_to_bucket("test.txt", "testing")
    