import random
import pandas as pd

def insere_randomico(lista, qtd_insercao):
    """
    Insere n elementos de acordo com a quantidade passada por parametro
    qtd_insercao: quantidade a ser inserida na lista
    lista: lista que recebera a insercao
    """
    for contador in range(qtd_insercao):
        lista.append(random.randint(1,qtd_insercao))
    random.shuffle(lista)
    return lista
    