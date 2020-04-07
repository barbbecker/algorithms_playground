def selection_sort(array):
    for i in range(len(array)):
        smaller =  i
        for j in range(i + 1, len(array)):
            # select the smaller value
            if array[j] < array[smaller]:
                smaller = j
        array[smaller], array[i] = array[i], array[smaller]
    return array


print(selection_sort([2, 7, 10, 14, 20]))