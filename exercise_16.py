def total_shopping_card(shopping_list):
    total = 0
    for x in shopping_list:
        y = str(x[1])
        pos = x[0] + "(" + y + ")"
        print(pos,"x", x[2], "  ", x[1]*x[2])
        total += x[1]*x[2]
    print("Do zapłaty", total )


shopping_list = [('mleko', 1.99, 2), ('chleb', 2.42, 3), ('masło', 5.99, 1), ('cola', 7.99, 3), ('ziemniaki', 0.99, 1.3)]
total_shopping_card(shopping_list)
# Wypisze
# mleko(1.99)       x 2     3.98
# chleb(2.42)       x 3     7.26
# masło(5.99)       x 1     5.99
# ziemniaki(0.99)   x 1.3   1.28
# Do zapłaty:              18.51
#
#w przykładzie zabrakło coli więc u mnie wyniki się różnią :)