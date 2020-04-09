def count(array):
    if array == []:
        return 0
    return 1 + count(array[1:])

print(count([3, 3, 3, 3]))