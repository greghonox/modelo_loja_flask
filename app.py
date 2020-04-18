"""
MODELO DE LOJA VIRTUAL FEITO EM FLASK PYTHON
GREGORIO HONORATO
"""

from flask import Flask
from paginas.home import home

app = Flask("--- LOJA VIRTUAL MODELO --- GREGÓRIO HONORATO")
### SITE
app.register_blueprint(home)



@app.before_first_request # OQUE FAZER QUANDO RODA A PRIMEIRA VEZ?
def __init__(): ...

app.run(debug=True, host='0.0.0.0')