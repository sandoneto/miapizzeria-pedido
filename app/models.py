from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class Pedidos(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    nome_cliente: so.Mapped[str] = so.mapped_column(sa.String(30), index=True)
    local_entrega: so.Mapped[str] = so.mapped_column(sa.String(50), index=True)
    vlr_entrega: so.Mapped[float] = so.mapped_column(sa.Float, index=True)
    vlr_total: so.Mapped[float] = so.mapped_column(sa.Float, index=True)
    
class ItensPedido(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    pedido_id: so.Mapped[int] = so.mapped_column(ForeignKey("Pedidos.id"))
    descricao: so.Mapped[str] = so.mapped_column(sa.String(30), index=True)
    quantidade: so.Mapped[int] = so.mapped_column(sa.I(50), index=True)
    
    vlr_entrega: so.Mapped[float] = so.mapped_column(sa.Float, index=True)
    
    vlr_total: so.Mapped[float] = so.mapped_column(sa.Float, index=True)