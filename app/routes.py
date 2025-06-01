from flask import render_template, Blueprint, request
from app import app, db
from app.models import Pedidos, ItensPedido
import sqlalchemy as sa
from jinja2 import TemplateNotFound

"""API Pedidos
        pedidos/ [GET] -> Carrega formulario de pedidos
        pedidos/ [POST] -> Cria novo pedido
        pedidos/list [GET] -> Carrega lista de todos os pedidos do dia
        pedidos/<id>/show [GET] -> Carrega informacoes de um pedido
        pedidos/<id>/cancel [UPDATE]
"""

def get_pedido(id):
    pass

pedidos = Blueprint('pedidos',__name__, url_prefix='/pedidos')

@pedidos.route('/', methods=['GET', 'POST'])
def create_pedido():
    
    if request.method == 'GET':
        return 'deu certo!!'
        pass
    
    data = request.get_json()
    print(data)
    pedido = Pedidos(nome_cliente = data['nomecliente'],
                     telefone = data['telefone'],
                     local_entrega = data['localentrega'],
                     vlr_entrega = data['vlrentrega'],
                     vlr_total = data['vlrtotal']
            )
    db.session.add(pedido)
    db.session.commit()
    id_pedido = pedido.id
    return id_pedido

@pedidos.route('/list', methods=['GET'])
def list_pedidos():
    return 'deu certo!!'
    pass

@pedidos.route('/<int:id>/show', methods=['GET'])
def show_pedido(id):
    return 'deu certo!!'
    pass

@pedidos.route('/<int:id>/cancel', methods=['UPDATE'])
def cancel_pedido(id):
    return 'deu certo!!'
    pass