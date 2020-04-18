import logging
from os import makedirs
from datetime import datetime
import logging.handlers as handlers

def criarPastas(pasta):
    try: makedirs(f'log/{pasta}/')
    except: pass

class DedoDuro:

    def dedar_registro(func):
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year
        hor = datetime.now().hour
        ARQUIVO = f"{dia}_{mes}_{ano}_{hor}.log/"
        pasta = f"{dia}_{mes}_{ano}/"

        criarPastas(pasta)
        arquivo = 'log/' + pasta + ARQUIVO

        logging.basicConfig(filename=arquivo, filemode='a',
        format="%(message)s %(pathname)s - %(filename)s - %(levelname)s - %(asctime)s")

        def method(*args):
            try:
                res = func(*args)
                logging.warning(res[1] if(isinstance(res, tuple)) else res)
                return  res
            except:
                print(f"*********************** ERRO ENCONTRADO {func.__name__} {args} ***********************")
                logging.error(f"*********************** ERRO ENCONTRADO {func.__name__} {args} ***********************")
            finally: logging.shutdown()

        return method