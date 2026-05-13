from flask import Blueprint, render_template, request
from banco.banco_fake import Usuarios

locacao_route = Blueprint('locacoes', __name__)

locacoes = Usuarios[0]['listaLocacao']
 
@locacao_route.route('/')
def listar_locacoes():
    return render_template('listar_locacoes.html', locacoes=locacoes)

@locacao_route.route('/', methods=['POST'])
def inserir_locacao():
    """ inserir os dados """
    data = request.json
    nova_locacao = {
        "id": len(locacoes) + 1,
        "nome": data['nome'],
        "descricao": data['descricao'],
        "valorDiaria": data['valorDiaria'],
    }
    locacoes.append(nova_locacao)
    return render_template('item_locacao.html', cliente=nova_locacao)

@locacao_route.route('/new')
def form_locacao():
    """ formulario para cadastrar """
    return render_template('form_locacao.html')

@locacao_route.route('/<int:locacao_id>')
def detalhar_locacao(locacao_id):  
    locacao = list(filter(lambda l: l['id'] == locacao_id, locacoes))[0]
    return render_template('detalhe_locacao.html', locacao=locacao)

@locacao_route.route('/<int:locacao_id>/edit')
def form_editar_locacao(locacao_id):
    """ formulario para editar """
    locacao = None
    for l in locacoes:
        if l['id'] == locacao_id:
            locacao = l
    return render_template('form_locacao.html', locacao=locacao)

@locacao_route.route('/<int:locacao_id>/update', methods=['PUT'])
def atualizar_locacao(locacao_id):
    """ atualizar informacoes """
    locacao_editada = None
    # obter dados do formulario de edicao
    data = request.json
    # obter usuario pelo id
    for l in locacoes:
        if l['id'] == locacao_id:
            l['nome'] = data['nome']
            l['descricao'] = data['descricao']
            l['valorDiaria'] = data['valorDiaria']
            locacao_editada = l
    # editar usuario
    return render_template('item_locacao.html', locacao=locacao_editada)

@locacao_route.route('/<int:locacao_id>/delete', methods=['DELETE'])
def deletar_locacao(locacao_id):   
    global locacoes
    locacoes = [ l for l in locacoes if l['id'] != locacao_id ]
    return {'deleted': 'ok'}