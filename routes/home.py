from flask import Blueprint, render_template

home_route = Blueprint('home', __name__)

@home_route.route('/')
def landing_page_home():
       return render_template('index.html')

@home_route.route('/login')
def login_page_home():
       return render_template('login.html')