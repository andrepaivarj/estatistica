import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

# Função para contar quantas vezes cada elemento aparece
def contagem(lista):
    cont = Counter(lista)
    s_casos = list(cont.keys())
    s_cont = list(cont.values())
    return s_cont, s_casos

# Função para calcular fi e fi %
def frequencia(s_cont, freq):
    fi = [v / freq for v in s_cont]
    fi_pc = [f"{v * 100:.2f}%" for v in fi]
    return fi, fi_pc

# Função para montar a tabela
def tabela(s_cont, s_casos, fi, fi_pc):
    dados = {
        'Nº de casos': s_cont,
        'Casos': s_casos,
        'fi': fi,
        'fi %': fi_pc
    }
    df = pd.DataFrame(data=dados)
    df.to_excel('tabela.xlsx', sheetname='Sheet1')

#Função para plotar o gráfico
def grafico(s_casos, fi, fi_pc):
    plt.bar(s_casos, fi)
    plt.xticks(ticks=s_casos, labels=s_casos)
    plt.yticks(ticks=fi, labels=fi_pc)
    plt.show()
    plt.savefig('nome.png')

# Função principal
def main():
    s = []
    freq = int(input('Insira o número do espaço amostral: '))

    for i in range(freq):
        ev_a = input(f'Insira a ocorrência {i+1} do evento A: ')
        s.append(ev_a)

    s_cont, s_casos = contagem(s)
    fi, fi_pc = frequencia(s_cont, freq)
    tabela(s_cont, s_casos, fi, fi_pc)
    grafico(s_casos,fi, fi_pc)

main()
