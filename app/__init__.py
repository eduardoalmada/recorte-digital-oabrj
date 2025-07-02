from flask import Flask
from dotenv import load_dotenv
from app.database import init_db
from app.tasks import tarefa_teste
import os

load_dotenv()

def create_app():
    app = Flask(__name__)

    # Configuração do banco de dados
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Inicializa o banco
    init_db(app)

    # Rota principal
    @app.route("/")
    def index():
        return "✅ Recorte Digital OABRJ rodando em produção!"

    # Rota de teste do Celery
    @app.route("/testar-celery")
    def testar_celery():
        tarefa_teste.delay()
        return "🚀 Tarefa Celery enviada com sucesso!"

    return app

