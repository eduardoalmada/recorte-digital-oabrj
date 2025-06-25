from flask import Flask
from dotenv import load_dotenv
import os
from app.tasks import tarefa_teste

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return "Recorte Digital OABRJ rodando em produção!"

@app.route("/ping")
def ping():
    return "pong"

@app.route("/testar-celery")
def testar_celery():
    tarefa_teste.delay()
    return "✅ Tarefa Celery enviada para o worker"
