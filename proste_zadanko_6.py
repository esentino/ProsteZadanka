def count_character(text, letter):
    if isinstance(letter, str) and len(letter) == 1:
        if isinstance(text, str):
            licznik = 0
            for character in text.upper():
                if character == letter.upper():
                    licznik += 1

            return licznik
        else:
            return "Podaj tekst źródłowy"
    else:
        return "Podaj jedną literę do zliczenia"


tekst = "Ala ma kota, kot ma Alę, a ja się wcale nie chwalę, że też mam Alę."
wystapienia_a = count_character(tekst, 'a')
print("Twoja litera w podanym tekście występuje "
      + str(wystapienia_a) + " razy.")
