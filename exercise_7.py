def count_all_characters(text):
    text = text.lower()
    slownik = {}
    for x in text:
        slownik[x] = text.count(x)
    return slownik
print(count_all_characters('Mam dzisiaj dobry humor'))
'''
Zwróci
{
    'm': 3,
    'a': 2,
    ' ': 3,
    'd': 2,
    'z': 1,
    'i': 2,
    's': 1,
    'j': 1,
    'o': 2,
    'b': 1,
    'r': 2,
    'y': 1,
    'h': 1,
    'u': 1,
    'r': 1
}
'''