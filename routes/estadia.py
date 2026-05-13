from flask import Blueprint, render_template, request
from banco.banco_fake import Usuarios

estadia_route = Blueprint('estadias', __name__)

estadias = Usuarios[0]['listaEstadias']

@estadia_route.route('/')
def listar_estadias():
    return render_template('listar_estadias.html', estadias=estadias)

@estadia_route.route('/', methods=['POST'])
def inserir_estadia():
    """ inserir os dados  """
    data = request.json
    nova_estadia = {
        "id": len(estadias) + 1,
        "id_cliente": data['id_cliente'],
        "id_locacao": data['id_locacao'],
        "dataInicial": data['dataInicial'],
        "dataFinal": data['dataFinal'],
    }
    estadias.append(nova_estadia)
    return render_template('item_estadia.html', estadia=nova_estadia)

@estadia_route.route('/new')
def form_estadia():
    """ formulario para cadastrar """
    return render_template('form_estadia.html')

@estadia_route.route('/<int:estadia_id>')
def detalhar_estadia(estadia_id):
    """ exibir detalhes  """
    estadia = list(filter(lambda e: e['id'] == estadia_id, estadias))[0]
    return render_template('detalhe_estadia.html', estadia=estadia)

@estadia_route.route('/<int:estadia_id>/edit')
def form_editar_estadia(estadia_id):
    """ formulario para editar  """
    estadia = None
    for e in estadias:
        if e['id'] == estadia_id:
            estadia = e
    return render_template('form_estadia.html', estadia=estadia)

@estadia_route.route('/<int:estadia_id>/update', methods=['PUT'])
def atualizar_estadia(estadia_id):
    """ atualizar informacoes  """
    estadia_editado = None
    # obter dados do formulario de edicao
    data = request.json
    # obter usuario pelo id
    for e in estadias:
        if e['id'] == estadia_id:
            e['id_cliente'] = data['id_cliente']
            e['id_locacao'] = data['id_locacao']
            e['dataInicial'] = data['dataInicial']
            e['dataFinal'] = data['dataFinal']
            estadia_editada = e     
    # editar 
    return render_template('item_estadia.html', estadia=estadia_editada)

@estadia_route.route('/<int:estadia_id>/delete', methods=['DELETE'])
def deletar_estadia(estadia_id):   
    global estadias
    estadias = [ e for e in estadias if e['id'] != estadia_id ]
    return {'deleted': 'ok'}