def regressive(i):
    print(i)
    if i <= 1: # caso-base
        return
    else: # caso recursivo
        regressive(i - 1) 

print(regressive(6))


## loop infinito
# def regressive1(i):
#     print(i)
#     regressive1(i - 1)

# print(regressive1(4))