from .celery_worker import celery

@celery.task
def tarefa_teste():
    print("🎉 Tarefa Celery executada com sucesso!")
    return "Executado"
