from random import randint


def domino(count):
    if isinstance(count, int) and count > 0:
        lista = []
        a, b = 0, 0
        for i in range(count):
            a = randint(0, 6)
            b = randint(0, 6)
            lista.append(str(a) + '-' + str(b))

        return lista

    else:
        return "Podaj nieujemną liczbę całkowitą"


kamienie = domino(10)
print(kamienie)
