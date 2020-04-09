def quicksort(array):
    if(len(array) < 2):
        return array # arrays com 0 ou 1 elementos ja estao ordenados
    else:
        pivo = array[0] # caso recursivo
        low = [i for i in array[1:] if i <= pivo] # subarray dos elementos menos que o pivo
        high = [i for i in array[1:] if i > pivo] # subarray dos elementos maiores que o pivo
    return quicksort(low) + [pivo] + quicksort(high)
    
print(quicksort([10, 56, 9, 4, 1, 6]))