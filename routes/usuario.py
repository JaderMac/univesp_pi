from flask import Blueprint, render_template 
from banco.fakeBd import Usuarios

usuario_route = Blueprint('usuario', __name__)
usuario_id = 5

@usuario_route.route('/')
def listar_usuarios():
    # Retorna todos usuarios do sistema // apenas admin
    usuariosd=Usuarios
    return render_template('listar_usuarios.html', usuariosd=Usuarios)

@usuario_route.route('/<int:usuario_id>')
def detalhar_usuario(usuario_id):
   usuario=Usuarios[usuario_id]
   return render_template('detalhar_usuario.html', usuario=usuario)

@usuario_route.route('/', methods=[('POST')])
def inserir_usuario():
    # Adiciona um usuario  // apenas admin
    pass

@usuario_route.route('/<int:usuario_id>/edit')
def form_atualizar_usuario(usuario_id):
    usuario=Usuarios[usuario_id]
    return render_template('form_atualizar_usuario.html', usuario=usuario)

@usuario_route.route('/<int:usuario_id>', methods=[('PUT')])
def atualizar_usuario(usuario_id):
    # Atualiza usuario
    pass

@usuario_route.route('/<int:usuario_id>/delete', methods=[('DELETE')])
def deletar_usuario(usuario_id):
    # Atualiza usuario // apenas admin
    pass