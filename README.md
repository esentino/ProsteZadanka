# ProsteZadanka

1. Napisz funkcję `sum_range(min, max)`, która zwróci sumę liczb całkowitych od `min` do `max` włącznie.

```py
print(sum_range(2,5)) # zwróci 14

print(sum_range(-2,2)) # zwróci 0
```

2. Napisz funkcję `min_and_max(lista)`, która przyjmuję listę liczb a zwraca krotkę z najmniejszą i największą liczbą z listy

```py
min_and_max([3,5,-3,12,-2,0]) # zwróci (-3, 12)

min_and_max([12]) # zwróci (12,12)

min_and_max([]) # zwróci (None, None)
```

3. Napisz funkcję `speed(distance, time)`, która policzy i zwróci średnią prędkość dla pokonanej drogi (`distance`) w metrach i czasu w sekundach (`time`). `Hint` użyj formatowanie stringa.

```py
speed(100,10) # zwróci 10 m/s
speed(2,10) # zwróci 0.2 m/s
```

4. Napisz funkcję `split_list(lista)`, która podzieli listę na dwie listy (pierwszy element do pierwszej drugi do drugiej, trzeci do pierwszej, czwarty do drugiej itd.) i zwróci jaką krotkę list.

```py
print(split_list([1,3,5,7,10,11,12,13]))
# Zwróci ([1,5,10,12], [3,7,11,13])
```

5. Napisz funkcję `multiply_list(lista, num)`, która pomnoży każdy element listy przez liczbę `num` i ją zwróci.

```py
print(multiply_list([3,5,2,6], 2))
# zwróci [6,10,4,12]
```

6. Napisz funkcję `count_character(text, letter)`, która zróci liczbę wystąpień podanej litery `letter` w tekscie `text`. Zliczamy duże i małe litery.

```py
print(count_character('Mam dzisiaj dobry humor', 'm'))
# zwróci 3
```

7. Napisz funkcję `count_all_characters(text)`, która zwróci słownik składający się z kluczy będących znakami w tekście, a wartościami liczbą wystąpień danej litery.

```py
print(count_all_characters('Mam dzisiaj dobry humor'))
'''
Zwróci
{
    'm': 3,
    'a': 2,
    ' ': 3,
    'd': 2,
    'z': 1,
    'i': 2,
    's': 1,
    'j': 1,
    'o': 2,
    'b': 1,
    'r': 2,
    'y': 1,
    'h': 1,
    'u': 1,
    'r': 1
}
'''
```

8. Napisz funkcję `policz_kotki(text)`, która zwróci liczbę wystąpień słowa kot w tekście.

```py
print(policz_kotki('Kotara to nie kotek, ale kotkiem jest Filemon'))
# zwróci 3
```

9. Napisz funkcję `domino(count)`, która zwróci listę z wylosowanymi kamieniami (ciąg znaków). Oznaczenie kamienia `a-b`, gdzie `a` i `b` to liczby z przedziału 0-6.

```py
print(domino(3))
# Zwróci np ['2-1', '0-3', '5-6']
```

10. Napisz funkcję `domino_tuple(count)`, która zamieni listę z poprzedniego zadania na listę tupli.

```py
print(domino_tuple(['2-1', '0-3', '5-6']))
# zwróci [(2,1), (0,3), (5,6)]
```

11. Napisz funkcję `own_who(transactions)`, która zwróci listę dłużników łącznie z kwotą. `transactions` jest to lista transakcji. Każda transakcja jest tuplą 3 elementową `('kto', 'komu', 'ile')`.

```py
transactions = [
    ('jacek', 'tomek', 20),
    ('tomek', 'natalia', 10),
    ('tomek', 'jacek', 30),
    ('natalia', 'jacek', 40)
]
print(own_who(transactions))
# zwróci 
[
    ('jacek', 'tomek', 10),
    ('natalia', 'tomek', 10),
    ('jacek', 'natalia', 40)
]
```

Opis przykładu: 
- jacek pożycza tomkowi 20 zł, następnie tomek pożycza jackowi 30 zł <-> w rezultacie jacek wisi tomkowi 10 zł
- tomek pożycza natalii 10 zł <-> w rezultacie natalia wisi tomkowi10 zł
- natalia pożycza jackowi 40 zł <-> w reultacie jacek wisi natalii 40 zł

12. Napisz funkcję `count_numbers(min, max)`, która zwróci ile liczb jest podzielnych przez 13 od `min` do `max` (włącznie).

13. Napisz funkcję `pokemon_text(text)`, która dla zadanego tekstu zwróci tekst pisany na przemian mała duża litera.

```py
print(pokemon_text("Mam dzisiaj wolne"))
# Zwróci MaM DzIsIaJ WoLnE
```

14. Napisz funkcję `divide_or_not_divide(by, not_by, max)`, która wyświetli listę liczb naturalnych podzielnych przez `by` a nie podzielnych przez `not_by` do `max`

```py
divide_or_not_divide(3,4,15)
# wyświetli:
# 3 6 9 15

divide_or_not_divide(2,3,13)
# wyświetli:
# 2 4 8 10
```

15. Napisz funkcję `dividers(number)`, która zwróci listę podzielniki danej liczby dodatniej. Dla `number` nie będącej liczbą całkowitą dodatnio zwróć `None`.

```py
print(dividers(24))
# zwróci [1,2,3,4,6,8,12,24]

print(dividers(0))
#zwróci None
```

16. Napisz funkcję `total_shopping_card(shopping_list)`, która wyświetli paragon.

```py
shopping_list = [
    ('mleko', 1.99, 2),
    ('chleb', 2.42, 3),
    ('masło', 5.99, 1),
    ('cola', 7.99, 3)
    ('ziemniaki', 0.99, 1.3)
    ]
total_shopping_card(shopping_list)
# Wypisze
# mleko(1.99)       x 2     3.98
# chleb(2.42)       x 3     7.26
# masło(5.99)       x 1     5.99
# ziemniaki(0.99)   x 1.3   1.28
# Do zapłaty:              18.51
#
```

17. Napisz funkcję `total_shopping_card_change(shopping_list, cash)`, która wyświetli paragon łącznie kwotą daną kasierowi oraz resztą.

```py
shopping_list = [
    ('mleko', 1.99, 2),
    ('chleb', 2.42, 3),
    ('masło', 5.99, 1),
    ('cola', 7.99, 3)
    ('ziemniaki', 0.99, 1.3)
    ]
total_shopping_card_change(shopping_list,20.00)
# Wypisze
# mleko(1.99)       x 2     3.98
# chleb(2.42)       x 3     7.26
# masło(5.99)       x 1     5.99
# ziemniaki(0.99)   x 1.3   1.28
# Do zapłaty:              18.51
# Zapłacono:               20.00
# Reszta:                   1.49
```

18. Napisz formularz w flasku, który pobierze od użytkownika 3 liczby, a następnie zwróci największą z nich do przeglądarki.

19. Napisz formularz w flasku, który pobierze od użytkownika zdanie. A następnie wyświetli jego długość.

20. Napisz funkcję do sprawdzania poprawności nazwiska:
- poprawne nazwisko ma conajmniej 3 litery
- nazwisko zaczyna się z dużej litery
- w nazwisku nie występuje spacja

Jeśli jakiś z warunków jest niespełniony rzuć wyjątkiem `ValueError`. Jeśli jest poprawne zwróć `True`.

21. Napisz formluarz w flasku, który pobierze od użytkownika zdanie. A następnie wyświetli wyrazy z tego zdania w kolejności alfabetycznej.

22. Napisz funkcję, która zamienia tekst podany w parametrze. W taki sposób, że małe litery zamienia na duże, a duże na małe.

23. Napisz funkcję, zwracająca same małe litery z podanego teksu jako parametr. 

24. Napisz funkcję `medjana(lista)`, zwracającą medianę dla podaj listy liczb, np.

```py
z = medjana([2,4,4,2,5])
print(z) # zwróci 4
x = medjana([3,2,2,3,5,2])
print(x) # zwróci 2.5
```

25. Napisz funkcję, która zwróci różnicę między średnią a medianą dla podanej listy liczb, np.

```py
k=diff_avg_medjana([2,4,4,2,5])
print(k) # zwróci 1 bo avg to 3 a mediana to 4
l=diff_avg_medjana([3,2,2,3,6,2])
print(l) # zwróci 0.5  bo avg to 3 a mediana to 2.5
```
