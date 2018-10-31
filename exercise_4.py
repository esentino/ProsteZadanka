def split_list(lista):
    lista1 = [x for x in lista[1::2]]
    lista2 = [x for x in lista[0::2]]
    return lista2 , lista1


print(split_list([1, 3, 5, 7, 10, 11, 12, 13]))
 # Zwróci ([1,5,10,12], [3,7,11,13])