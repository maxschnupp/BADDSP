from httplib2 import error
from google.cloud import storage
import httplib2
import constants

RETRYABLE_ERRORS = (httplib2.HttpLib2Error, IOError)

def retry_upload(blob, source_file_name, base_directory):
    try: 
        blob.upload_from_filename("{}/{}".format(base_directory, source_file_name))
        print(
            "File {} uploaded to {}.".format(
                source_file_name, "{}-{}".format(tag, source_file_name)
            )
        )
    except:
        print("Error on retry upload aborted")
    

def upload_to_gin_bucket(source_file_name, tag):
    storage_client = storage.Client()
    bucket = storage_client.bucket(constants.GIN_BUCKET_NAME)
    blob = bucket.blob("{}-{}".format(tag, source_file_name))
    try:
        blob.upload_from_filename("{}/{}".format(constants.SAVE_DIR, source_file_name))
        print(
            "File {} uploaded to {}.".format(
                source_file_name, "{}-{}".format(tag, source_file_name)
            )
        )
    except RETRYABLE_ERRORS as err:
        print("an error occured uploading the file {}: {}".format(source_file_name, err))
        retry_upload(blob, source_file_name, constants.SAVE_DIR)


def upload_to_audio_bucket(source_file_name, tag):
    storage_client = storage.Client()
    bucket = storage_client.bucket(constants.AUDIO_BUCKET_NAME)
    blob = bucket.blob("{}-{}".format(tag, source_file_name))
    try:
        blob.upload_from_filename("{}/{}".format(constants.AUDIO_OUTPUT, source_file_name))
        print(
            "File {} uploaded to {}.".format(
                source_file_name, "{}-{}".format(tag, source_file_name)
            )
        )
    except RETRYABLE_ERRORS as err:
        print("an error occured uploading the file {}: {}".format(source_file_name, err))
        retry_upload(blob, source_file_name, constants.AUDIO_OUTPUT)


