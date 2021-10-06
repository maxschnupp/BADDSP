from google.cloud import storage
import constants

def upload_to_gin_bucket(source_file_name, tag):
    storage_client = storage.Client()
    bucket = storage_client.bucket(constants.GIN_BUCKET_NAME)
    blob = bucket.blob("{}-{}".format(tag, source_file_name))
    blob.upload_from_filename("{}/{}".format(constants.SAVE_DIR, source_file_name))
    print(
        "File {} uploaded to {}.".format(
            source_file_name, "{}-{}".format(tag, source_file_name)
        )
    )

def upload_to_audio_bucket(source_file_name, tag):
    storage_client = storage.Client()
    bucket = storage_client.bucket(constants.AUDIO_BUCKET_NAME)
    blob = bucket.blob("{}-{}".format(tag, source_file_name))
    blob.upload_from_filename("{}/{}".format(constants.AUDIO_OUTPUT, source_file_name))
    print(
        "File {} uploaded to {}.".format(
            source_file_name, "{}-{}".format(tag, source_file_name)
        )
    )