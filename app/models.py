from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Advogado(db.Model):
    __tablename__ = 'advogados'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    numero_oab = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    whatsapp = db.Column(db.String(20), nullable=False)

class Publicacao(db.Model):
    __tablename__ = 'publicacoes'
    id = db.Column(db.Integer, primary_key=True)
    advogado_id = db.Column(db.Integer, db.ForeignKey('advogados.id'), nullable=False)
    titulo = db.Column(db.String(500), nullable=False)
    descricao = db.Column(db.Text)
    data_publicacao = db.Column(db.Date)
    link = db.Column(db.String(1000))
