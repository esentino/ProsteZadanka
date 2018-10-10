def min_and_max(lista):
    if not lista:
        t=(None,None)
        return t
    else:
        minimum=min(lista)
        maximum=max(lista)
        t=(minimum,maximum)
        return t

r1=min_and_max([3,5,-3,12,-2,0]) # zwróci (-3, 12)
r2=min_and_max([12]) # zwróci (12,12)
r3=min_and_max([]) # zwróci (None, None)
print(r1)
print(r2)
print(r3)
