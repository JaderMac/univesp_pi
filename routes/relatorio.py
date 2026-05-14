from flask import Blueprint, render_template, request
from banco.banco_fake import Usuarios

relatorio_route = Blueprint('relatorios', __name__)

relatorios = [
    {"id":1, "id_locacao":1, "dataInicial":"27/07/2028", "dataFinal":"28/07/2028", "valorFinal": 120},
    {"id":2, "id_locacao":5, "dataInicial": "27/07/2028", "dataFinal":"28/07/2028", "valorFinal": 550},
    {"id":3, "id_locacao":9, "dataInicial": "27/07/2028", "dataFinal":"28/07/2028", "valorFinal": 2700}]

@relatorio_route.route('/')
def listar_relatorios():
    return render_template('listar_relatorios.html', relatorios=relatorios)

@relatorio_route.route('/', methods=['POST'])
def inserir_relatorio():
    """ inserir os dados  """
    data = request.json
    nova_relatorio = {
        "id": len(relatorios) + 1,
        "id_cliente": data['id_cliente'],
        "id_locacao": data['id_locacao'],
        "dataInicial": data['dataInicial'],
        "dataFinal": data['dataFinal'],
    }
    relatorios.append(nova_relatorio)
    return render_template('item_relatorio.html', relatorio=nova_relatorio)

@relatorio_route.route('/new')
def form_relatorio():
    """ formulario para cadastrar """
    return render_template('form_relatorio.html')

@relatorio_route.route('/<int:relatorio_id>')
def detalhar_relatorio(relatorio_id):
    """ exibir detalhes  """
    relatorio = list(filter(lambda e: e['id'] == relatorio_id, relatorios))[0]
    return render_template('detalhe_relatorio.html', relatorio=relatorio)

@relatorio_route.route('/<int:relatorio_id>/edit')
def form_editar_relatorio(relatorio_id): 
    """ formulario para editar  """
    relatorio = None
    for e in relatorios:
        if e['id'] == relatorio_id:
            relatorio = e
    return render_template('form_relatorio.html', relatorio=relatorio)

@relatorio_route.route('/<int:relatorio_id>/update', methods=['PUT'])
def atualizar_relatorio(relatorio_id):
    """ atualizar informacoes  """
    relatorio_editado = None
    # obter dados do formulario de edicao
    data = request.json
    # obter usuario pelo id
    for e in relatorios:
        if e['id'] == relatorio_id:
            e['id_cliente'] = data['id_cliente']
            e['id_locacao'] = data['id_locacao']
            e['dataInicial'] = data['dataInicial']
            e['dataFinal'] = data['dataFinal']
            relatorio_editada = e     
    # editar 
    return render_template('item_relatorio.html', relatorio=relatorio_editada)

@relatorio_route.route('/<int:relatorio_id>/delete', methods=['DELETE'])
def deletar_relatorio(relatorio_id):   
    global relatorios
    relatorios = [ e for e in relatorios if e['id'] != relatorio_id ]
    return {'deleted': 'ok'}