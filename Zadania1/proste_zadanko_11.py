
def own_who(transactions):
    if isinstance(transactions, list):
        transakcje = transactions.copy()
        dluznicy_lista = []

        while transakcje:                                        # dopóki lista nie jest pusta:
            a, b, c = transakcje[0]                              # pobieram transakcję
            transakcje.pop(0)                                    # usuwam pobraną transakcję, żeby nie dublować

            for trans in transakcje:
                if trans[0] == a and trans[1] == b:              # jeśli transakcja w tę samą stronę
                    c += trans[2]                                # dodać
                    transakcje.pop(transakcje.index(trans))      # usuwam transakcję z listy
                elif trans[0] == b and trans[1] == a:            # jeśli transakcja w drugą stronę
                    c -= trans[2]                                # odjąć
                    transakcje.pop(transakcje.index(trans))      # usuwam transakcję z listy

            if c > 0:                                            # przypisanie do nowej listy dłużników
                dluznicy_lista.append([b, a, c])
            elif c < 0:
                dluznicy_lista.append([a, b, -c])
            else:
                dluznicy_lista.append([b, a, 0])

        for i, n in enumerate(dluznicy_lista):                  # zamiana list wewnątrz listy na krotki
            dluznicy_lista[i] = tuple(n)

        return dluznicy_lista


    else:
        return "Podaj listę transakcji"


transactions = [
    ('jacek', 'tomek', 20),
    ('tomek', 'natalia', 10),
    ('tomek', 'jacek', 30),
    ('natalia', 'jacek', 40),
    ('igor', 'piotr', 100),
    ('piotr', 'igor', 45),
    ('piotr', 'natalia', 20),
    ('jacek', 'igor', 30)
]

dlugi = own_who(transactions)

print(dlugi)
