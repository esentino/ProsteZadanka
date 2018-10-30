def domino_tuple(count):
    if isinstance(count, list):
        lista_krotek = []
        for element in count:
            a, b = element.split("-")
            lista_krotek.append((int(a), int(b)))

        return lista_krotek

    else:
        return "Podaj listę domino"


lista = ['6-4', '3-4', '3-5', '0-4', '4-0', '1-1', '4-2', '5-0', '2-1', '6-4']
print(domino_tuple(lista))
