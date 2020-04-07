# -*- coding: utf-8 -*-
# ordenação por seleção
# ------------------------------------------------
# 1 - armazena o menor valor
# 2 - armazena o indice do menor valor


def busca_menor(array):
    menor = array[0] # 1
    indice_menor = 0 # 2
    for i in range(1, len(array)):
        if array[i] < menor:
            menor = array[i]
            indice_menor = i
    return indice_menor


def ordenacao_por_selecao(array):
    novo_array = []
    for i in range(len(array)):
        menor = busca_menor(array) # encontra o menor elemento do array e add ao novo array
        novo_array.append(array.pop(menor))
    return novo_array


print(ordenacao_por_selecao([5, 3, 6, 2, 10]))