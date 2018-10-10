def pokemon_text(text):
    text2 = ""
    licznik = 0
    for x in text:
        if licznik == 0 or licznik % 2 == 0:
            x = x.upper()
            text2 += x
            licznik += 1
        else:
            text2 += x
            licznik += 1
    return text2

print(pokemon_text("Mam dzisiaj wolne"))
# Zwróci MaM DzIsIaJ WoLnE