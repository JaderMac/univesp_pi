from flask import Blueprint, render_template 
from banco.fakeBd import locacoes

locacao_route = Blueprint('locacao', __name__)

locacao_id = 1

@locacao_route.route('/')
def listar_locacao():
    locacoesdoc = locacoes
    return render_template('listar_locacao.html', locacoesdoc = locacoes)

@locacao_route.route('/<int:locacao_id>')
def detalhar_locacao(locacao_id):
    locacao = locacoes[locacao_id]
    return render_template('detalhar_locacao.html', locacao=locacao)

@locacao_route.route('/', methods=[('POST')])
def inserir_locacao():
    # Adiciona uma locacao
    pass

@locacao_route.route('/<int:locacao_id>/edit')
def form_atualizar_locacao(locacao_id):
    locacao = locacoes[locacao_id]
    return render_template('form_atualizar_locacao.html', locacao=locacao)

@locacao_route.route('/<int:locacao_id>', methods=[('PUT')])
def atualizar_locacao(locacao_id):
    # Atualiza locacao
    pass

@locacao_route.route('/<int:locacao_id>/delete', methods=[('DELETE')])
def deletar_locacao(locacao_id):
    # deleta locacao
    pass