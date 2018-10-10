def divide_or_not_divide(by, not_by, max):
    lista_l = ""
    for x in range(max + 1):
        if x == 0 or (x % by == 0 and x % not_by != 0):
            lista_l+= str(x) + " "
        else:
            pass
    print(lista_l)
divide_or_not_divide(3,4,15)
# wyświetli:
# 0 3 6 9 15

divide_or_not_divide(2,3,13)
# wyświetli:
# 0 2 4 8 10