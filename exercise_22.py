def duzemale(tekst):
    wynik=""
    for x in tekst:
        if x.isupper():
            wynik += x.lower()
        else:
            wynik += x.upper()
    return wynik

print(duzemale("tO jeSt tEst"))