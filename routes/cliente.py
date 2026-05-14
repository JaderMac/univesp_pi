from flask import Blueprint, render_template, request
from banco.banco_fake import Usuarios
 
cliente_route = Blueprint('clientes', __name__)

clientes = Usuarios[0]['listaClientes'] 

@cliente_route.route('/')
def listar_clientes():
    return render_template('listar_clientes.html', clientes=clientes)
    
@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """ inserir os dados do cliente """
    data = request.json
    novo_cliente = {
        "id": len(clientes) + 1,
        "nome": data['nome'],
        "celular": data['celular'],
        "email": data['email'],
    }
    clientes.append(novo_cliente)
    return render_template('item_cliente.html', cliente=novo_cliente)
    
@cliente_route.route('/new')
def form_cliente():
    """ formulario para cadastrar um cliente """
    return render_template('form_cliente.html')
    
@cliente_route.route('/<int:cliente_id>')
def detalhar_cliente(cliente_id):
    """ exibir detalhes do cliente """
    cliente = list(filter(lambda c: c['id'] == cliente_id, clientes))[0]
    return render_template('detalhe_cliente.html', cliente=cliente)
    
@cliente_route.route('/<int:cliente_id>/edit')
def form_editar_cliente(cliente_id):
    """ formulario para editar um cliente """
    cliente = None
    for c in clientes:
        if c['id'] == cliente_id:
            cliente = c
    return render_template('form_cliente.html', cliente=cliente)

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    """ atualizar informacoes do cliente """
    cliente_editado = None
    # obter dados do formulario de edicao
    data = request.json
    # obter usuario pelo id
    for c in clientes:
        if c['id'] == cliente_id:
            c['nome'] = data['nome']
            c['celular'] = data['celular']
            c['email'] = data['email']
            cliente_editado = c     
    # editar usuario
    return render_template('item_cliente.html', cliente=cliente_editado)

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):   
    global clientes
    clientes = [ c for c in clientes if c['id'] != cliente_id ]
    return {'deleted': 'ok'}