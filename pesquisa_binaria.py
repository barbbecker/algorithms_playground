# -*- coding: utf-8 -*-
# pesquisa binária - só funciona quando a lista esta ordenada
# ----------------------------------------------------------------
# baixo e alto acompanham a parte da lista que vc esta procurando
# Enquanto ainda nao conseguiu chegar a um unico elemento, verifica o elemento central
# Acha o item
# O chute foi muito alto
# O chute foi muito baixo
# O item nao existe
# Listas comecam no 0, o proximo elemento tem indice 1

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto:
        meio = (baixo + alto)/2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None


# quando chama o metodo, retorna o indice da posicao do numero que colocou em item
minha_lista = [1, 3, 5, 7, 9]
print(pesquisa_binaria(minha_lista, 7))
print(pesquisa_binaria(minha_lista, -1))