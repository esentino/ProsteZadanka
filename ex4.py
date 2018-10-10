def split_list(lista):
    l1=[]
    l2=[]
    for i in lista:
        if lista.index(i)%2==0:
            l1.append(i)
        else:
            l2.append(i)
    t=()
    t=(l1,l2)
    return t

r=split_list([1,3,5,7,10,11,12,13])
print(r)
# Zwróci ([1,5,10,12], [3,7,11,13])
# even=parzysty

