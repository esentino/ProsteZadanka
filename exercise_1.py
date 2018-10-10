def sum_range(min, max):
    suma = 0
    for x in range(min,max+1):
        suma += x
    return suma
#
# print(sum_range(2, 5))  # zwróci 14
# print(sum_range(-2, 2))  # zwróci 0
# print(sum_range(-4, -2))  # zwróci 0