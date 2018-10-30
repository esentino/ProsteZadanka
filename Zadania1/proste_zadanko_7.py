def count_all_characters(text):
    if isinstance(text, str):
        dctnry = {}
        characters = list(text.lower())
        for char in characters:
            licznik = 0
            if char not in dctnry.keys():
                for letter in text.lower():
                    if letter == char:
                        licznik += 1
                dctnry[char] = licznik

        return dctnry

    else:
        return "Podaj tekst źródłowy"


tekst = "Ala ma kota, kot ma Alę, a ja się wcale nie chwalę, że też mam Alę."
tekst2 = "Mam dzisiaj dobry humor"
litery = count_all_characters(tekst)
litery2 = count_all_characters(tekst2)
print(litery)
print(litery2)
