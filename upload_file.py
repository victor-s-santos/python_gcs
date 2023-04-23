import os
import argparse
import logging
from decouple import config
from google.cloud import storage

credentials = config("GOOGLE_APPLICATION_CREDENTIALS")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

def connect_to_bucket(bucket_name="my-first-bucket_test"):
    """Realize the connection with gcs bucket

    Args:
        bucket_name (str, optional): The disered bucket name. Defaults to "my-first-bucket_test".

    Returns:
        _type_: The storage.Client object to be used to make the upload. 
    """
    return storage.Client().bucket(bucket_name)

def upload_file_to_bucket(bucket_name="my-first-bucket_test", upload_file_name="README.pdf"):
    """Realize the upload file to gcs bucket

    Args:
        bucket_name (str, optional): The disered bucket name. Defaults to "my-first-bucket_test".
        upload_file_name (str, optional): The disered file to be uploeaded. Defaults to "README.pdf".
    """
    try:
        bucket = connect_to_bucket(bucket_name)
        blob = bucket.blob(upload_file_name)
        blob.upload_from_filename(upload_file_name)
        logging.info(f"Arquivo {upload_file_name} enviado com sucesso!")
    
    except Exception as e:
        logging.error(f"Ocorreu um erro {e} ao enviar o arquivo {upload_file_name}!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--bucket", help="Bucket name", required=True)
    parser.add_argument("-n", "--file_name", help="Upload File Name", required=True)
    args = parser.parse_args()

    upload_file_to_bucket(bucket_name=args.bucket, upload_file_name=args.file_name)

