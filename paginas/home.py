"""
MODELO DE LOJA VIRTUAL FEITO EM FLASK PYTHON
GREGORIO HONORATO
"""
from flask import Blueprint
home = Blueprint('home', __name__)

@home.route('/')
def index(): 
    return "INICIO"