def tylkomale(tekst):
    wynik=""
    for x in tekst:
        if x.islower():
            wynik = wynik + x + " "
    return wynik

# print(tylkomale("tO jeSt tE2st."))