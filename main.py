import sys
import os
from heapsort import heap_sort
from heapsort_iterativo import heap_sort_interativo
from radix_sort import radixSort
from utils import insere_randomico
from gera_relatorio import gera_csv_resultado, plot_grafico
import time
import random
import pandas as pd


def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Grafico  heap sort ")
    print("2. Gera csv com relatório dos tempos de ordenação dos algoritmos")
    print("3. Sair")
    print(67 * "-")


def seleciona_algoritmo(algoritmo, lista, tempo_ordenacao, nome_algoritmo):
    for i in range(1000,11000, 1000):
        inicio_cronometagem = time.time()
        algoritmo(lista)
        fim_cronometragem = time.time()
        tempo_cronometragem = fim_cronometragem - inicio_cronometagem
        tempo_ordenacao[nome_algoritmo][i] = tempo_cronometragem
        insere_randomico(lista, 1000)    

if __name__ == '__main__':
    loop=True
    tempo_ordenacao_python = {'heap_sort': {1000: 0, 2000: 0,
                  3000: 0, 4000: 0, 5000: 0, 6000: 0,
                  7000: 0, 8000: 0, 9000: 0, 10000: 0},
                   'heap_sort': {}, 'heap_sort_iterativo': {},'radix_sort': {} }
    # tempo_ordenacao_python['merge_sort'].update(tempo_ordenacao_python['bucket_sort'])
    # tempo_ordenacao_python['quick_sort'].update(tempo_ordenacao_python['bucket_sort'])
    tempo_ordenacao_python['heap_sort'].update(tempo_ordenacao_python['heap_sort'])
    tempo_ordenacao_python['heap_sort_iterativo'].update(tempo_ordenacao_python['heap_sort'])
    tempo_ordenacao_python['radix_sort'].update(tempo_ordenacao_python['heap_sort'])

    tamanho_vetor = 10000    

    while loop:
        print_menu()
        choice = input("Entre sua opcao [1-3]: ")
        if choice=='1':     
            print("Opcao 1 foi escolhida")
            lista = random.sample(range(0,tamanho_vetor * 2), tamanho_vetor)
            seleciona_algoritmo(heap_sort, lista, tempo_ordenacao_python, 'heap_sort')
            seleciona_algoritmo(heap_sort_interativo, lista, tempo_ordenacao_python, 'heap_sort_iterativo')
            # seleciona_algoritmo(radixSort, lista, tempo_ordenacao_python, 'radix_sort')
            plot_grafico(tempo_ordenacao_python)
        elif choice=='2':
            print("Opcao 1 foi escolhida")
            lista = random.sample(range(0,tamanho_vetor * 2), tamanho_vetor)
            seleciona_algoritmo(heap_sort, lista, tempo_ordenacao_python, 'heap_sort')
            seleciona_algoritmo(heap_sort_interativo, lista, tempo_ordenacao_python, 'heap_sort_iterativo')
            gera_csv_resultado(tempo_ordenacao_python)
        elif choice=='3':
            print("Opcao 3 foi escolhida")
            print('Saindo....')
            loop=False
        else:
            input("Opcao incorreta. Aperte qualquer tecla para tentar novamente..")