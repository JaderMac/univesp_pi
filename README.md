# Projeto integrador

Sistema de gestão de locações

--

1 - Puxar o projeto para a sua máquina.

2 - Criar um ambiente virtual na sua máquina.

    python -m venv venv

3 - Instalar as dependencias do projeto.

    pip install -r requirements.txt

4 - Rodar o arquivo main

    python main.py

---

Rotas finalizadas:

    Index
        http://127.0.0.1:5000/

    Listar
        http://127.0.0.1:5000/usuario/
        http://127.0.0.1:5000/usuario/clientes/
        http://127.0.0.1:5000/usuario/locacoes/
        http://127.0.0.1:5000/usuario/estadias/ 

    Atualizar
        http://127.0.0.1:5000/usuario/clientes/1/edit
        http://127.0.0.1:5000/usuario/estadias/1/edit
        