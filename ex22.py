# sprint ;) :) :D
def change(text):
    return text.swapcase()


# slow food ;)
def change1(text):
    t = list(text)
    i=0
    while i <len(t):
        if t[i].isupper():
            t[i]=t[i].lower()
        else:
            t[i]=t[i].upper()
        i+=1
        result="".join(t)
    return result


print(change("Ola ma kota Olka a Basia ma psa Mańka"))
print(change1("Ola ma kota Olka a Basia ma psa Mańka"))
print(change("LOWER AnD upper"))
print(change1("LOWER AnD upper"))