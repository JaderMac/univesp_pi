from banco.banco_fake import Usuarios
usuario = Usuarios[0]
clientes = usuario['listaClientes']
# clientes = usuario.get("listaClientes")
print(clientes)