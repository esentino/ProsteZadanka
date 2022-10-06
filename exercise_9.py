import random
def domino(count):
    lista = []
    for x in range(count):
        a = str(random.randint(0,6))
        b = str(random.randint(0,6))
        c = a +"-" + b
        lista.append(c)
    return lista
print(domino(3))
# Zwróci np ['2-1', '0-3', '5-6']