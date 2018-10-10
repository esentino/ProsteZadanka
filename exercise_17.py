def total_shopping_card_change(shopping_list, cash):
    total = 0
    for x in shopping_list:
        y = str(x[1])
        pos = x[0] + "(" + y + ")"
        print(pos,"x", x[2], "  ", x[1]*x[2])
        total += x[1]*x[2]
    print("Do zapłaty", total )
    print("Zapłacono", cash )
    print("Reszta", cash - total )


shopping_list = [('mleko', 1.99, 2), ('chleb', 2.42, 3), ('masło', 5.99, 1), ('cola', 7.99, 3), ('ziemniaki', 0.99, 1.3)]
total_shopping_card_change(shopping_list,50.00)
# Wypisze
# mleko(1.99)       x 2     3.98
# chleb(2.42)       x 3     7.26
# masło(5.99)       x 1     5.99
# ziemniaki(0.99)   x 1.3   1.28
# Do zapłaty:              18.51
# Zapłacono:               20.00
# Reszta:                   1.49
#w przykładzie zabrakło coli więc u mnie wyniki się różnią :)