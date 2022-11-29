import re

def own_who(transactions):
    result=[]
    for i in transactions:
        r1=[item[2]-i[2] for item in transactions if item[1] == i[0] and item[0]==i[1]]
        if not r1:
            r2=0
        else:
            r2=int(r1[0])
        if r2>0:
            tuple1=(i[0],i[1],r1[0])
            result.append(tuple1)
        elif r2<0:
            pass
        else:
            tuple1=(i[1],i[0],i[2])
            result.append(tuple1)

    return result



transactions = [
    ('jacek', 'tomek', 20),
    ('tomek', 'natalia', 10),
    ('tomek', 'jacek', 30),
    ('natalia', 'jacek', 40)
]

transactions2 = [
    ('jacek', 'tomek', 20),
    ('tomek', 'natalia', 10),
    ('tomek', 'jacek', 30),
    ('natalia', 'jacek', 40),
    ('jacek', 'natalia', 25)
]


print(own_who(transactions))
print(own_who(transactions2))


# transactions = [
#     ('jacek', 'tomek', 20),
#     ('tomek', 'natalia', 10),
#     ('tomek', 'jacek', 30),
#     ('natalia', 'jacek', 40)
# ]
# print(own_who(transactions))
# # zwróci
# [
#     ('jacek', 'tomek', 10),
#     ('natalia', 'tomek', 10),
#     ('jacek', 'natalia', 40)
# ]
#
# Opis przykładu:
#
#     jacek pożycza tomkowi 20 zł, następnie tomek pożycza jackowi 30 zł <-> w rezultacie jacek wisi tomkowi 10 zł
#     tomek pożycza natalii 10 zł <-> w rezultacie natalia wisi tomkowi10 zł
#     natalia pożycza jackowi 40 zł <-> w reultacie jacek wisi natalii 40 zł
