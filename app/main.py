from flask import Blueprint, jsonify
from app.tasks import exemplo_tarefa_celery

routes = Blueprint('routes', __name__)

@routes.route('/testar-celery', methods=['GET'])
def testar_celery():
    exemplo_tarefa_celery.delay()
    return jsonify({'status': 'Tarefa enviada para o worker Celery!'})
