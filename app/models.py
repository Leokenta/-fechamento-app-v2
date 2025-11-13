from app import db
from datetime import datetime

class Fechamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(100), nullable=False)
    data = db.Column(db.Date, nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    quantidade = db.Column(db.Float, nullable=False)
    cor = db.Column(db.String(50))
    valor_unitario = db.Column(db.Float, nullable=False)
    desconto = db.Column(db.Float, default=0.0)
    valor_total = db.Column(db.Float, nullable=False)
    valor_total_final = db.Column(db.Float, nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, cliente, data, descricao, quantidade, cor, valor_unitario, desconto):
        self.cliente = cliente
        self.data = data
        self.descricao = descricao
        self.quantidade = quantidade
        self.cor = cor
        self.valor_unitario = valor_unitario
        self.desconto = desconto or 0.0
        self.valor_total = quantidade * valor_unitario
        self.valor_total_final = self.valor_total - self.desconto
