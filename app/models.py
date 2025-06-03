import datetime
from typing import Optional, List
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class Pedidos(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    nome_cliente: so.Mapped[str] = so.mapped_column(sa.String(30), index=True)
    telefone: so.Mapped[str] = so.mapped_column(sa.String(11), index=True)
    local_entrega: so.Mapped[str] = so.mapped_column(sa.String(50), index=True)
    itens_pedido: so.Mapped[List["ItensPedido"]] = so.relationship(back_populates="pedido")
    status: so.Mapped[str] = so.mapped_column(sa.String(1), index=True, default='c')
    vlr_entrega: so.Mapped[float] = so.mapped_column(sa.Float, index=True)
    vlr_total: so.Mapped[float] = so.mapped_column(sa.Float, index=True)
    criado: so.Mapped[datetime.datetime] = so.mapped_column(sa.TIMESTAMP, default=datetime.datetime.utcnow)
    modificado: so.Mapped[datetime.datetime] = so.mapped_column(sa.TIMESTAMP, default=datetime.datetime.utcnow)
    
    def __repr__(self):
        return '<Pedido {}>'.format(self.id)
    
class ItensPedido(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    pedido_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Pedidos.id), index=True)
    pedido: so.Mapped["Pedidos"] = so.relationship(back_populates="itens_pedido")
    descricao: so.Mapped[str] = so.mapped_column(sa.String(30), index=True)
    quantidade: so.Mapped[int] = so.mapped_column(sa.Integer(), index=True)
    vlr_unit: so.Mapped[float] = so.mapped_column(sa.Float, index=True)
    vlr_total: so.Mapped[float] = so.mapped_column(sa.Float, index=True)
    
    def __repr__(self):
        return '<ItensPedido {}>'.format(self.descricao)