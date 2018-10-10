def dividers(number):
    return_list=[]
    if isinstance(number,int) and number>0:
        for i in range(1,number+1):
            if number%i==0:
                return_list.append(i)
        return return_list
    else:
        return None


print(dividers(24))
# zwróci [1,2,3,4,6,8,12,24]

print(dividers(0))
#zwróci None

print(dividers(5))
print(dividers(-1))