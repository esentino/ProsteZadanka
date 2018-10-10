def count_numbers(min, max):
    k=0
    for i in range(min,max+1):
        if i%13==0:
            k+=1
    return k


print(count_numbers(0,13))
print(count_numbers(0,26))
print(count_numbers(0,39))
print(count_numbers(0,52))
print(count_numbers(0,6))
print(count_numbers(0,25))
print(count_numbers(0,53))
print(count_numbers(50,53))
