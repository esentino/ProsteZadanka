def pokemon_text(text):
    t=list(text)
    for i in t:
        if t.index(i)%2==0:
            t[t.index(i)]=i.upper()
        else:
            t[t.index(i)]=i.lower()
    return "".join(t)

print(pokemon_text("Mam dzisiaj wolne"))
# Zwróci MaM DzIsIaJ WoLnE