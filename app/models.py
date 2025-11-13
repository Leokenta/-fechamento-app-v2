from app import db
from datetime import datetime

class Fechamento(db.Model):
    __tablename__ = 'fechamentos'  # 👈 isso é essencial!

    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(200), nullable=False)
    data = db.Column(db.Date, nullable=False)
    descricao = db.Column(db.Text)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    quantidade = db.Column(db.Integer)
    preco_unitario = db.Column(db.Numeric(12, 2))
    cor = db.Column(db.String(100))
    desconto = db.Column(db.Numeric(12, 2))
    valor_sem_desconto = db.Column(db.Numeric(12, 2))
    valor_final = db.Column(db.Numeric(12, 2))

    def __repr__(self):
        return f"<Fechamento {self.cliente} - {self.data}>"
