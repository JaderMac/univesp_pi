from flask import Blueprint, render_template
from banco.banco_fake import Usuarios

home_route = Blueprint('home', __name__)

@home_route.route('/')
def landing_page_home():
       usuario=Usuarios[0]
       return render_template('index.html',usuario=usuario)

@home_route.route('/login')
def login_page_home():
       return render_template('login.html')