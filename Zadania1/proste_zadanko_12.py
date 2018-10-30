def count_numbers(min, max):
    if (isinstance(i, int) for i in [min, max]) and (min and max) > 0:

        licznik = 0

        for i in range (min, max + 1):
            if i % 13 == 0:
                licznik += 1

        return licznik

    else:
        return "Podaj niezerowe liczby całkowite"


policz = count_numbers(12, 1123)
print(policz)
