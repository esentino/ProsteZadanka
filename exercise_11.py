def own_who(transactions):
    slownik = {}
    slownik2 = {}
    for x in transactions:
        slownik[str(x[1]),str(x[0])] = int(x[2])
        slownik2[str(x[1]),str(x[0])] = int(x[2])
    for klucz in slownik:
        rev_klucz = klucz[::-1]
        if rev_klucz not in slownik2:
            pass
        else:
            wart = slownik[klucz]
            del slownik2[klucz]
            rew_wart = slownik[rev_klucz]
            if wart <= rew_wart:
                now_wart = rew_wart - wart
                slownik2[rev_klucz] = now_wart
            else:
                now_wart = wart - rew_wart
                slownik2[klucz] = now_wart
    return (slownik2)

transactions = [
    # ('jacek', 'tomek', 40),
    ('jacek', 'tomek', 20),
    ('tomek', 'natalia', 10),
    ('tomek', 'jacek', 30),
    # ('tomek', 'jacek', 10),
    ('natalia', 'jacek', 40)
]
print(own_who(transactions))