# -*- coding: utf-8 -*-
# binary search - só funciona quando a lista esta ordenada
# ----------------------------------------------------------------
# baixo e alto acompanham a parte da lista que vc esta procurando
# Enquanto ainda nao conseguiu chegar a um unico elemento, verifica o elemento central
# Acha o item
# O chute foi muito alto
# O chute foi muito baixo
# O item nao existe
# Listas comecam no 0, o proximo elemento tem indice 1

def binary_search(received_list, item):
    low = 0
    high = len(received_list) - 1
    while low <= high:
        middle = (low + high)/2
        shot = received_list[middle]
        if shot == item:
            return middle
        if shot > item:
            high = middle - 1
        else:
            low = middle + 1
    return None


# quando chama o metodo, retorna o indice da posicao do numero que colocou em item
my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 7))
print(binary_search(my_list, -1))