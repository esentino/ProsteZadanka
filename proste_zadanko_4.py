def split_list(lista):
    if isinstance(lista, list):
        return lista[::2], lista[1::2]
    else:
        return "Podaj listę do podziału."


some_list = [1, 2, 3, "Antoni", 3, 5, "Krisztian", ("Ala", "kot"),
             ["Mścisław", "Sędziwój", 25], 6, 987, False]

splitted_list = split_list(some_list)
print(splitted_list)
