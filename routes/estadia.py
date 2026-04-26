from flask import Blueprint, render_template 
from banco.fakeBd import estadias
from banco.fakeBd import clientes
from banco.fakeBd import locacoes

estadia_route = Blueprint('estadia', __name__)

estadia_id = 0

@estadia_route.route('/')
def listar_estadia():
    estadiasd=estadias
    return render_template('listar_estadias.html', estadiasd=estadias)

@estadia_route.route('/<int:estadia_id>')
def detalhar_estadia(estadia_id):
   estadia=estadias[estadia_id]
   cliente=clientes[1]
   locacao=locacoes[1]
   return render_template('detalhar_estadia.html', estadia=estadia, cliente=cliente, locacao=locacao)

@estadia_route.route('/', methods=[('POST')])
def inserir_estadia():
    # Adiciona uma estadia 
    pass

@estadia_route.route('/<int:estadia_id>/edit')
def form_atualizar_estadia(estadia_id):
    estadia=estadias[estadia_id]
    cliente=clientes[1]
    locacao=locacoes[1]
    return render_template('form_atualizar_estadia.html', estadia=estadia, cliente=cliente, locacao=locacao)

@estadia_route.route('/<int:estadia_id>', methods=[('PUT')])
def atualizar_estadia(estadia_id):
    # Atualiza estadia
    pass

@estadia_route.route('/<int:estadia_id>/delete', methods=[('DELETE')])
def deletar_estadia(estadia_id):
    # Atualiza estadia
    pass