def split_list(lista):
    lista1 = []
    lista2 = []

    for i, elem in enumerate(lista):
        if i % 2 == 0:
            lista1.append(elem)
        else:
            lista2.append(elem)

    return lista1, lista2


print(split_list([1, 3, 5, 7, 10, 11, 12, 13]))
# Zwróci ([1,5,10,12], [3,7,11,13])
