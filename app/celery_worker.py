import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

celery = Celery("recorte",
    broker=os.getenv("REDIS_URL"),
    backend=os.getenv("REDIS_URL")
)

celery.conf.timezone = "America/Sao_Paulo"
