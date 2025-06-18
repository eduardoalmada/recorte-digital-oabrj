# Recorte Digital OABRJ - Produção

Sistema de envio automático de publicações do DJERJ para advogados da OABRJ via WhatsApp, usando Flask, Celery, PostgreSQL e Z-API.

## Estrutura
- Flask API (Gunicorn)
- Celery + Redis
- Banco PostgreSQL
- Integração com Z-API

## Deploy no Render
1. Subir o código no GitHub
2. Criar Web Service (usa `web:` do Procfile)
3. Criar Background Worker (usa `worker:` do Procfile)
4. Adicionar Redis e PostgreSQL como serviços conectados
5. Configurar variáveis com base no `.env.example`
