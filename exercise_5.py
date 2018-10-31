def multiply_list(lista, num):
    lista_w = [ x * num for x in lista]
    return lista_w
# przykład z listą składaną

print(multiply_list([3, 5, 2, 6], 2))
# zwróci [6,10,4,12]