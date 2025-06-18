from .db import db

class Advogado(db.Model):
    __tablename__ = 'advogados'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    oab = db.Column(db.String)
    telefone = db.Column(db.String)

class Publicacao(db.Model):
    __tablename__ = 'publicacoes'
    id = db.Column(db.Integer, primary_key=True)
    nome_citado = db.Column(db.String)
    oab_citada = db.Column(db.String)
    data = db.Column(db.Date)
    conteudo = db.Column(db.Text)
    link = db.Column(db.String)
    enviada = db.Column(db.Boolean, default=False)

class LogEnvio(db.Model):
    __tablename__ = 'logs_envio'
    id = db.Column(db.Integer, primary_key=True)
    advogado_id = db.Column(db.Integer)
    publicacao_id = db.Column(db.Integer)
    status = db.Column(db.String)
    horario = db.Column(db.String)
