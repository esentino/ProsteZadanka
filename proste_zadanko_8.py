def policz_kotki(text):
    if isinstance(text, str):

        licznik = 0
        words = text.split()

        for word in words:
            if 'kot' in word.lower():
                licznik += 1

        return licznik

    else:
        return "Podaj tekst źródłowy"


tekst = "Ala ma kota, kot ma Alę, a ja się wcale nie chwalę, że też mam Alę."
tekst2 = "Kotara to nie kotek, ale kotkiem jest Filemon"
tekst3 = "Kot kot KoT koT kOT KOT kOt"

liczba_kotkow = policz_kotki(tekst)
liczba_kotkow2 = policz_kotki(tekst2)
liczba_kotkow3 = policz_kotki(tekst3)
print(liczba_kotkow, liczba_kotkow2, liczba_kotkow3, sep='\n')
