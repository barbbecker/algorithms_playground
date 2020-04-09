def max(array):
    if len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]
    max_value =  max(array[1:])
    return array[0] if array[0] > max_value else max_value

print(max([1, 2, 3, 4, 10]))