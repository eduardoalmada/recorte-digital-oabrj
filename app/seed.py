from app import create_app
from app.models import db, Advogado

app = create_app()

with app.app_context():
    db.session.query(Advogado).delete()

    advogados = [
        Advogado(
            nome="Daniel Soares Motta",
            numero_oab="123456",
            email="daniel@example.com",
            whatsapp="+5521999999999"
        ),
        Advogado(
            nome="Ivan dos Santos Gonçalves",
            numero_oab="654321",
            email="ivan@example.com",
            whatsapp="+5521988888888"
        ),
        Advogado(
            nome="Leandro Terra Oliveira Comyn do Amaral",
            numero_oab="112233",
            email="leandro@example.com",
            whatsapp="+5521977777777"
        )
    ]

    db.session.bulk_save_objects(advogados)
    db.session.commit()

    print("✅ Advogados inseridos com sucesso.")
