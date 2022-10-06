def count_numbers(min, max):
    licznik = 0
    for x in range(min, max + 1):
        if x % 13 == 0:
            licznik+= 1
        else:
            pass
    return licznik
# print(count_numbers(13,39))
