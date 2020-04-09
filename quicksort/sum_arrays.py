def sum(array):
    total = 0
    for x in array:
        total += x
    return total

print(sum([1, 2, 3, 4]))
    
# soma recursiva do array
def sum2(array):
    if array == []:
        return 0
    return array[0] + sum2(array[1:])

print(sum2([4, 5, 5]))