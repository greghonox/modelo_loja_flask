import sqlite3
from datetime import datetime

class Conexao:
    global dialogo
    dialogo = f"ARVORE DA VIDA || {datetime.now()}"

    def conexao_banco(func, db='arvore.db'):
        def method(*args):
            try:
                cmd = func(args[0])
                banco = sqlite3.connect(db)
                banco.execute(cmd)
                banco.commit()
                return f"\n{dialogo} COMANDO EXECUTADO C/ SUCESSO: {cmd}\n"
            except Exception as erro: return f"\n\n*******ERRO C/ BANCO DE DADOS: (|{erro}|) COMANDO EXECUTADO:{cmd} *********\n\n"
            finally: banco.close()
        return method

    def conexao_banco_s_arg(func, db='arvore.db'):
        def method(*args):
            try:
                cmd = func()
                banco = sqlite3.connect(db)
                banco.execute(cmd)
                banco.commit()
                return f"\n{dialogo} COMANDO EXECUTADO C/ SUCESSO: {cmd}\n"
            except Exception as erro: return f"\n\n*******ERRO C/ BANCO DE DADOS: {erro} COMANDO EXECUTADO:{cmd} *********\n\n"
            finally: banco.close()
        return method

    def pegar_dados(func, db='arvore.db'):
        def method(*args):
            try:
                banco = sqlite3.connect(db)
                cmd = func(args[0])
                res = banco.execute(cmd).fetchall()
                banco.close()
                return (res, f"\n{dialogo} COMANDO SENDO EXECUTADO: {cmd}\n")
            except Exception as erro: return f"\n{dialogo} COMANDO SENDO EXECUTADO: {cmd}\n"
            finally: banco.close()
        return method
