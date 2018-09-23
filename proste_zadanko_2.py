from numbers import Number


def min_and_max(lista):
    if not lista:
        return None, None

    if isinstance(lista, list):
        for element in lista:
            if isinstance(element, Number):
                pass
            else:
                return "Jest lista, ale poproszę w niej tylko liczby :)"

        minimal = lista[0]
        maximal = lista[len(lista) - 1]

        if len(lista) == 1:
            return lista[0], lista[0]

        else:
            for element in lista:
                if element < minimal:
                    minimal = element
                if element > maximal:
                    maximal = element
            return minimal, maximal

    else:
        return "Podaj listę liczb."


print(min_and_max([]))
print(min_and_max([13]))
print(min_and_max([1, 4]))
print(min_and_max([4, 1]))
print(min_and_max([3, 3]))
print(min_and_max([0, 4]))
print(min_and_max([-4, 4]))
print(min_and_max([4, -6]))
print(min_and_max([-12, 9]))
print(min_and_max([1, 4, 45, -69, 256, -123]))
print(min_and_max(12))
print(min_and_max("Zbychu"))
print(min_and_max([12, "Krzychu"]))
print(min_and_max([2, True]))           # logiczna 1
print(min_and_max([False, -23]))        # logiczne 0


