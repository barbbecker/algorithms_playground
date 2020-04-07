# -*- coding: utf-8 -*-
# Selection sort
# ------------------------------------------------
# 1 - armazena o menor valor
# 2 - armazena o indice do menor valor


def minor_search(array):
    smaller = array[0] # 1
    lower_index= 0 # 2
    for i in range(1, len(array)):
        if array[i] < smaller:
            smaller = array[i]
            lower_index = i
    return lower_index


def selection_sort(array):
    new_array = []
    for i in range(len(array)):
        smaller = minor_search(array) # encontra o menor elemento do array e add ao novo array
        new_array.append(array.pop(smaller))
    return new_array


print(selection_sort([5, 3, 6, 2, 10]))