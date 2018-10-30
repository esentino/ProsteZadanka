def total_shopping_card(shopping_list):
    komunikat = ""
    total = 0
    for item in shopping_list:
        a, b, c = item
        d = b * c
        total += d
        komunikat += "{0:10} ({1:0.2f}) x {2:0.2f} {3:>12.2f} \n".format(a, b, c, d)

    komunikat += "Do zapłaty: {:>25.2f}".format(total)
    print(komunikat)


lista_zakupow = [
    ('mleko', 1.99, 2),
    ('chleb', 2.42, 3),
    ('masło', 5.99, 1),
    ('cola', 7.99, 3),
    ('ziemniaki', 0.99, 1.3)
    ]

total_shopping_card(lista_zakupow)