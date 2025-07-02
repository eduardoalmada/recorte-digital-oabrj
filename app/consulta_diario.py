import requests
from datetime import datetime
from app.models import Publicacao, db

API_URL = "https://api-publica.datajud.cnj.jus.br/api_publica_tjrj/_search"
API_KEY = "cDZHYzlZa0JadVREZDJCendQbXY6SkJlTzNjLV9TRENyQk1RdnFKZGRQdw=="
HEADERS = {
    "Authorization": f"APIKey {API_KEY}",
    "Content-Type": "application/json"
}

def buscar_publicacoes_para(advogado):
    query = {
        "query": {
            "bool": {
                "must": [
                    {"match_phrase": {"nome_parte": advogado.nome}},
                    {"match_phrase": {"numero_oab": advogado.numero_oab}}
                ]
            }
        },
        "sort": [{"data_publicacao": {"order": "desc"}}],
        "size": 10
    }

    response = requests.post(API_URL, headers=HEADERS, json=query)

    if response.status_code != 200:
        print(f"Erro ao consultar DataJud para {advogado.nome}")
        return []

    resultados = response.json().get("hits", {}).get("hits", [])
    novas_publicacoes = []

    for item in resultados:
        fonte = item.get("_source", {})
        titulo = fonte.get("assunto", "Publicação sem título")
        descricao = fonte.get("resumo", "")
        data_str = fonte.get("data_publicacao", "")
        data_publicacao = datetime.strptime(data_str, "%Y-%m-%d") if data_str else None
        link = fonte.get("link_processo", "")

        # Evita duplicatas
        existente = Publicacao.query.filter_by(
            advogado_id=advogado.id,
            titulo=titulo,
            data_publicacao=data_publicacao
        ).first()

        if not existente:
            publicacao = Publicacao(
                advogado_id=advogado.id,
                titulo=titulo,
                descricao=descricao,
                data_publicacao=data_publicacao,
                link=link
            )
            db.session.add(publicacao)
            novas_publicacoes.append(publicacao)

    if novas_publicacoes:
        db.session.commit()
        print(f"✅ {len(novas_publicacoes)} novas publicações para {advogado.nome}")

    return novas_publicacoes
