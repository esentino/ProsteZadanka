def sum_range(min, max):
    s=0
    for i in range(min,max+1):
        s+=i
    return s

r=sum_range(2,5) # zwróci 14
r1=sum_range(-2,2) # zwróci 0
print("Suma liczb całkowitych wynosi: {}".format(r))
print("Suma liczb całkowitych wynosi: {}".format(r1))
