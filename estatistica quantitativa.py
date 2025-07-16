from collections import Counter
import pandas as pd
from matplotlib import pyplot as plt


#Função que conta a quantidade de ocorrencias do evento A
def contagem(lista):
    cont = Counter(lista)
    s_casos = list(cont.keys())
    s_cont = list(cont.values())
    return s_cont, s_casos

#Função que determina a frequência relativa de cada ocorrencia do evento A
def freq_relativa(s_cont, freq):
    fi = [v / freq for v in s_cont]
    fi_pc = [f"{v * 100:.2f}%" for v in fi]
    return fi, fi_pc

#Função que determina a frequência absoluta de cada ocorrência do evento A
def freq_abs(s_cont, freq):
    fama = []
    fame = []
    acumuladoma = 0
    for i in s_cont:
        acumuladoma += i
        fama.append(acumuladoma)
    acumuladome = sum(s_cont)
    fame.append(acumuladome)  # Começa com total
    for j in s_cont:
        acumuladome -= j
        if acumuladome > 0:
            fame.append(acumuladome)
        else:
            break  # parar antes do zero

    fabsme = [p / freq for p in fame]
    fabsme_pc = [f"{p * 100:.2f}%" for p in fabsme]
    fabsma = [v/ freq for v in fama]
    fabsma_pc = [f"{v * 100:.2f}%" for v in fabsma]
    return fama, fabsma, fabsma_pc, fame, fabsme, fabsme_pc

#Função que determina a tabela em formato (.csv) por pandas
def tabela(s_cont, s_casos, fi, fi_pc,fama, fabsma, fabsma_pc, fame, fabsme, fabsme_pc):
    dados = {
        "Casos": s_casos,
        'Nº de casos': s_cont,
        'Fi': fi,
        'Fi %': fi_pc,
        'Fa+': fama,
        'fa+': fabsma,
        'fa+ %': fabsma_pc,
        'Fa-': fame,
        'fa-': fabsme,
        'fa- %': fabsme_pc

    }
    df = pd.DataFrame(data=dados)
    print(df)

#Função que plota os gráficos de frequência relativa e frequência relativa acumulada
def graficos(s_casos, fi, fabsma, fabsme) -> None:
    plt.plot(s_casos, fabsma, label='Fa+ (Relativa Acumulada Crescente)')
    plt.plot(s_casos[:len(fabsme)], fabsme, label='Fa- (Relativa Acumulada Decrescente)')
    plt.xlabel('Casos')
    plt.ylabel('Frequência Relativa Acumulada')
    plt.legend()
    plt.show()

    plt.bar(s_casos, fi)
    plt.xlabel('Casos')
    plt.ylabel('Frequencia Relativa')
    plt.show()

#Função Principal
def main():
    s = []
    freq = int(input('Insira o número do espaço amostral: '))

    for i in range(freq):
        ev_a = int(input(f'Insira a ocorrência {i+1} do evento A: '))
        s.append(ev_a)
    s_cont, s_casos = contagem(s)
    # Ordena os casos em ordem crescente mantendo os pares
    s_casos, s_cont = zip(*sorted(zip(s_casos, s_cont)))
    s_casos = list(s_casos)
    s_cont = list(s_cont)
    fi, fi_pc = freq_relativa(s_cont, freq)
    fama, fabsma, fabsma_pc, fame, fabsme, fabsme_pc = freq_abs(s_cont, freq)
    tabela(s_cont, s_casos, fi, fi_pc,fama, fabsma, fabsma_pc, fame, fabsme, fabsme_pc)
    graficos(s_casos, fi, fabsma, fabsme)

main()
