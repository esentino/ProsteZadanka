from random import randint

def domino(count):
    r=[]
    i=0
    while i<count:
        a = randint(0, 6)
        b = randint(0, 6)
        r.append("{}-{}".format(a,b))
        i+=1
    return r

def domino_tuple(count):
    list1=domino(count)
    result=[]
    i=0
    while i<count:
        a=(int(list1[i][0]))
        b=(int(list1[i][2]))
        tuple1=(a,b)
        result.append(tuple1)
        i+=1
    #print(list1)
    return result

print(domino_tuple(3))
#print(domino_tuple(['2-1', '0-3', '5-6']))
# zwróci [(2,1), (0,3), (5,6)]