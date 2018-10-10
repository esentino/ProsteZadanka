def domino_tuple(lista):
    mylist_str = " ".join(lista) #zamiana na stringa, elemeny odzielone znakiem spacji
    mylist_str = mylist_str.replace("-",",")
    mylist_lis = mylist_str.split(" ")
    wynik = []
    for x in mylist_lis:
        y = int(x[0])
        z = int(x[2])
        v = (y,z)
        wynik.append(v)
    return wynik
print(domino_tuple(['2-1', '0-3', '5-6']))
# zwróci [(2,1), (0,3), (5,6)]