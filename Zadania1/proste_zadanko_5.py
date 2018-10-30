def multiply_list(lista, num):
    if isinstance(num, int) and num > 0:
        if isinstance(lista, list):
            nowa_lista = [i * num for i in lista]
            return nowa_lista
        else:
            return "Podaj listę"
    else:
        return "Podaj nieujemny całkowity mnożnik"


nowa_lista = [1, 2, 3, "Ha", 1, 8]
pomnozona_lista = multiply_list(nowa_lista, 15)
print(pomnozona_lista)
