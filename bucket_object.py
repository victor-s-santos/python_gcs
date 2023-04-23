import os
import logging
from decouple import config
from google.cloud import storage

credentials = config("GOOGLE_APPLICATION_CREDENTIALS")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

class BucketObject:

    def __init__(self):
        self.storage_client = storage.Client()

    def list_files(self, bucket_name="my-first-bucket_test"):
        files_list = self.storage_client.list_blobs(bucket_name)
        logging.info([file.name for file in files_list])
    
    def download_file(self, file_name, object_name, bucket_name="my-first-bucket_test"):
        try:
            bucket = self.storage_client.bucket(bucket_name)
            blob = bucket.blob(object_name)
            blob.download_to_filename(file_name)
            logging.info(f"Arquivo {file_name} baixado com sucesso!")
        
        except Exception as e:
            logging.info(f"Ocorreu um erro {e} ao baixar o arquivo {file_name}")


if __name__ == "__main__":
    c = BucketObject()

    print("Listando arquivos:")
    c.list_files()

    print("...")
    print("\n")
    print("Baixando o arquivo requeriments.txt:")
    c.download_file(object_name="requerimentos.txt", file_name="requirementos.txt")
