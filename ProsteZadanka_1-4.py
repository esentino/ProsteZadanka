# Zadanie 1

def sum_range(min, max):
    suma = 0
    for i in range(min, max+1):
        suma += i
    return suma

print(sum_range(2,5))
print(sum_range(-2,2))

# Zadanie 2

def min_and_max(lista):
    if not lista:
        return (None, None)
    else:
        minimum = lista[0]
        maximum = lista[0]
        for element in lista:
            if element < minimum:
                minimum = element
            if element > maximum:
                maximum = element
        return (minimum,maximum)

b = [3,5,-3,12,-2,0]
c = [5]
d = []

print(min_and_max(b))
print(min_and_max(c))
print(min_and_max(d))

# Zadanie 3

def speed(distance,time):
    return str(round(distance/time)) + " m/s"
print(speed(100,10))


# Zadanie 4

def split_list(z):
    l_1 = []
    l_2 = []
    for element in z:
        if z.index(element) % 2 == 0:
            l_1.append(element)
        else:
            l_2.append(element)
    x = (l_1,l_2)
    return x

y = [1,3,5,7,10,11,12,13]

print(split_list(y))









