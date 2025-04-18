from flask import render_template, Blueprint, request
from app import app
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
    if request.method == 'POST':
        pass
    pass

@pedidos.route('/list', methods=['GET'])
def list_pedidos():
        pass

@pedidos.route('/<int:id>/show', methods=['GET'])
def show_pedido(id):
    pass

@pedidos.route('/<int:id>/cancel', methods=['UPDATE'])
def cancel_pedido(id):
    pass
            