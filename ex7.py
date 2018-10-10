from collections import OrderedDict,Counter

# wersja z biblioteką collections i metodą Counter
def count_character(text, letter):
    t=text.lower()
    count=Counter(t)
    r=count[letter]
    return r

# Wersja ze zwykłym dict() i niewiadomą kolejnoscią wyswietlania par klucz:wartosc
def count_all_characters1(text):
    dict1= dict()
    for i in text:
        i=i.lower()
        if i not in dict1.keys():
            dict1[i]=count_character(text,i)
    return dict1

# Wersja z OrderedDict() czyli pierwotną kolejnością wstawiania par klucz:wartosc do słownika,
# tak by kolejnosc elementów była wyświetlona zgodnie z trescia zadania
def count_all_characters2(text):
    dict1= OrderedDict()
    for i in text:
        i=i.lower()
        if i not in dict1.keys():
            dict1[i]=count_character(text,i)
    return dict1

d=dict()
d=count_all_characters1('Mam dzisiaj dobry humor')
print(d)
d=count_all_characters2('Mam dzisiaj dobry humor')
print(d)
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