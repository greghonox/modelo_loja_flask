from jwt import decode
from flask import jsonify, request, redirect


CHAVE_SECRETA = "JESUS_VOLTARA_PARA_NOS_RESGATAR_DESSE_MUNDO"

def validar_sessao(f):
    def method(*args):
        try:
            token = request.cookies.get('token')
            decode(token, CHAVE_SECRETA)
            return f(*args)
        except Exception as erro: return redirect('/login')
    return method
