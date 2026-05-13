import boto3
import botocore.config
import os
from dotenv import load_dotenv
from botocore.exceptions import ClientError
from logging import Logger, FileHandler, Formatter, DEBUG
from datetime import datetime

# Cargar variables de entorno
load_dotenv()

# Configuración de Logging
logger = Logger("minio_client")
file_handler = FileHandler("logs.log")
file_handler.setLevel(DEBUG)
formatter = Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def upload_to_minio():
    # Obtener credenciales del .env
    endpoint = "http://localhost:9000"
    access_key = os.getenv("MINIO_ACCESS_KEY", "minioadmin")
    secret_key = os.getenv("MINIO_SECRET_KEY", "minioadmin")
    bucket_name = "test-bucket"

    try: 
        client = boto3.client(
            "s3",
            endpoint_url=endpoint,
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            config=botocore.config.Config(
                signature_version="s3v4",
                s3={"addressing_style": "path"},
            ),
        )
        
        # 1. Verificar si el bucket existe, si no, crearlo
        try:
            client.head_bucket(Bucket=bucket_name)
        except ClientError:
            logger.info(f"El bucket {bucket_name} no existe. Creándolo...")
            client.create_bucket(Bucket=bucket_name)

        # 2. Definir el nombre del archivo (corregido para coincidir con el scraper)
        today_str = datetime.now().strftime('%Y-%m-%d')
        file_name = f"whales_{today_str}.csv"
        file_path = f"data/{file_name}"
        
        # 3. Subir el archivo
        with open(file_path, "rb") as f:
            client.upload_fileobj(f, bucket_name, file_name)
        
        logger.info(f"Archivo {file_name} subido correctamente al bucket {bucket_name}")
        print(f"✅ Éxito: {file_name} subido a MinIO.")

    except FileNotFoundError as e:
        logger.error(f"No se encontró el archivo local {file_path}: {e}")
        print(f"❌ Error: No se encontró el archivo {file_path}. ¿Corriste el scraper primero?")
    except ClientError as e:
        logger.error(f"Error de conexión con MinIO: {e}")
        print(f"❌ Error de MinIO: {e}")
    except Exception as e:
        logger.error(f"Error inesperado: {e}")
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    upload_to_minio()
