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

print(domino(3))
# Zwróci np ['2-1', '0-3', '5-6']

