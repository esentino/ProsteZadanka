def domino_tuple(lista):
    print(lista)
    mylist = " ".join(lista) #zamiana na stringa, elemeny odzielone znakiem spacji
    mylist = mylist.replace("-",",")
    mylist = mylist.split(" ")
    # mylist = tuple(mylist)
    # mylist = ' '.join(lista).replace('-', ',').split()
    # mylist = tuple(mylist)
    print(mylist)
    print(type(mylist))
print(domino_tuple(['2-1', '0-3', '5-6']))
# zwróci [(2,1), (0,3), (5,6)]