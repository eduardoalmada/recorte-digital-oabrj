import os
import requests

def enviar_mensagem(telefone, mensagem):
    instance_id = os.getenv("ZAPI_INSTANCE_ID")
    token = os.getenv("ZAPI_TOKEN")
    url = f"https://api.z-api.io/instances/{instance_id}/token/{token}/send-text"

    payload = {
        "phone": telefone,
        "message": mensagem
    }

    response = requests.post(url, json=payload)
    return response.json()
