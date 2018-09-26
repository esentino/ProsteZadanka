def total_shopping_card_change(shopping_list, cash):
    komunikat = ""
    total = 0
    reszta = 0
    for item in shopping_list:
        a, b, c = item
        d = b * c
        total += d
        komunikat += "{0:10} ({1:0.2f}) x {2:0.2f} {3:>12.2f} \n".format(a, b, c, d)

    reszta = cash - total
    komunikat += "Do zapłaty: {:>25.2f}\n".format(total)
    if reszta < 0:
        komunikat += "Masz za mało pieniędzy!"
    else:
        komunikat += "Zapłacono: {:>26.2f}\n".format(cash)
        komunikat += "Reszta: {:>29.2f}\n".format(reszta)
    print(komunikat)


lista_zakupow = [
    ('mleko', 1.99, 2),
    ('chleb', 2.42, 3),
    ('masło', 5.99, 1),
    ('cola', 7.99, 3),
    ('ziemniaki', 0.99, 1.3)
    ]

total_shopping_card_change(lista_zakupow, 60)
