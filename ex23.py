# sprint ;) :) :D
def to_lower(text):
    return text.lower()


# slow food ;)
def to_lower1(text):
    t = list(text)
    i=0
    while i <len(t):
        if t[i].isupper():
            t[i]=t[i].lower()
        i+=1
        result="".join(t)
    return result

print(to_lower("Ola ma kota Olka a Basia ma psa Mańka"))
print(to_lower1("Ola ma kota Olka a Basia ma psa Mańka"))
print(to_lower("LOWER AnD upper"))
print(to_lower1("LOWER AnD upper"))