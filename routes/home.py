from flask import Blueprint, render_template
from banco.banco_fake import Usuarios

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home_page_home():
       return render_template('index.html')

@home_route.route('/login')
def login_page_home():
       return render_template('login.html')

@home_route.route('/landing')
def landing_page_home():
       return render_template('landing.html')

@home_route.route('/meus_clientes')
def clientes_page():
       return render_template('meus_clientes.html')

@home_route.route('/minhas_locacoes')
def locacoes_page():
       return render_template('minhas_locacoes.html')

@home_route.route('/minhas_estadias')
def estadias_page():
       return render_template('minhas_estadias.html')