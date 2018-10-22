def pokemon_text(text):
    if isinstance(text, str):
        lista = []
        output = ""
        for i in range(len(text)):
            if i % 2 == 0:
                lista.append(text[i].upper())
            else:
                lista.append(text[i].lower())

        for element in lista:
            output += element

        return output

    else:
        return "Podaj tekst źródłowy"


tekst = "Ala ma kota, kot ma Alę, a ja się wcale nie chwalę, że też mam Alę."
pokemon = pokemon_text(tekst)
print(pokemon)
