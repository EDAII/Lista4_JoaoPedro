import matplotlib.pyplot as plt
import pandas as pd
import csv

def gera_csv_resultado(tempo_ordenacao):
    """
    Gera csv de resultados
    tempo_ordenacao: dicionario com tempos de ordenacao dos algoritmos
    nome_linguagem: string com nome da linguagem de implementação do algoritmo
    """
    df = pd.DataFrame(tempo_ordenacao)
    nome_arquivo = 'resultados_algoritmos.csv'
    df.to_csv(nome_arquivo)

def plot_grafico(tempo_ordenacao):
    """
    Plota gráfico de Tempo(s) x tamanho vetor por algoritmos de uma determinada linguagem
    tempo_ordenacao: dicionario com tempos de ordenacao dos algoritmos
    nome_linguagem: string com nome da linguagem de implementação do algoritmo
    """
    pd.DataFrame(tempo_ordenacao).plot(kind='line')
    titulo_grafico = 'Grafico Tempo(s) x Tamanho vetor'
    plt.title(titulo_grafico)
    plt.ylabel('Tempo(s)')
    plt.xlabel('Tamanho vetor')
    plt.show()