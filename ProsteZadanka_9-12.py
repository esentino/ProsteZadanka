
# Zadanie 9

def domino(count):
    r = []
    for i in range(count):
        a = randint(0, 6)
        b = randint(0, 6)
        r.append(f"{a}-{b}")
    return r

print(domino(3))

# Zadanie 10


def domino_tuple(count):
    lista = domino(count)
    changed = []
    i = 0
    while i < count:
        a = int(lista[i][0])
        b = int(lista[i][2])
        tuple_created = (a, b)
        changed.append(tuple_created)
        i += 1
    return changed

print(domino_tuple(3))


# Zadanie 11

def own_who(transactions):
    pass


# Zadanie 12

def count_numbers(min, max):
     list = [x for x in range(min, max) if x % 13 == 0]
     r = 0
     for i in list:
          r += 1
     return r

print(count_numbers(13, 55))




