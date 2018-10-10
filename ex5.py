def multiply_list(lista, num):
    result=[]
    for i in lista:
        result.append(i*num)
    return result


print(multiply_list([3, 5, 2, 6], 2))
# zwróci [6,10,4,12]