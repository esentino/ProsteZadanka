def dividers(number):
    lista_l = []
    if number < 1 or type(number) != int :
        return None
    else:
        for x in range(1,number + 1):
            if number % x == 0 :
                lista_l.append(x)
            else:
                pass
        return lista_l

print(dividers(24))
# zwróci [1,2,3,4,6,8,12,24]

print(dividers(0))
#zwróci None


