def divide_or_not_divide(by, not_by, max):
    for i in range(0,max+1):
        if i%by==0 and i%not_by!=0:
            print(i, end=' ')
    print("\n")

divide_or_not_divide(3,4,15)
# wyświetli:
# 0 3 6 9 15
# BŁĄD!! wyświetli:
# 3 6 9 15
# bo 0 też jest podzielne przez 4 a wynikiem mają być liczby podzielne przez 3 ale niepodzielne przez 4
# 0 będzie podzielne przez każdą liczbę

divide_or_not_divide(2,3,13)
# wyświetli:
# 0 2 4 8 10
# BŁĄD!! wyświetli:
# 2 4 8 10
# bo 0 też jest podzielne przez 4 a wynikiem mają być liczby podzielne przez 3 ale niepodzielne przez 4
# 0 będzie podzielne przez każdą liczbę