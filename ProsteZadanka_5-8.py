
from collections import Counter

# Zadanie 5

def multiply_list(lista, num):
    l = []
    for element in lista:
        calculated = element * num
        l.append(calculated)
    return l

print(multiply_list([3,5,2,6], 2))


# Zadanie 6

def count_character(text, letter):
    if isinstance(text, str) and isinstance(letter, str):
        count = 0
        for element in text:
            element.lower()
            if element == letter:
                count += 1
    else:
        return "Podaj string!"
    return count

print(count_character('Mam dzisiaj dobry humor', 'h'))


# Zadanie 7

def count_all_characters(text):
    low = text.lower()
    return {i:low.count(i) for i in low}


print(count_all_characters('Mam dzisiaj dobry humor'))


# Zadanie 8

def policz_kotki(text):
    t = text.lower()
    k = 'kot'
    if k in t:
        count_cats = t.count(k)
        return count_cats


print(policz_kotki('Kotara to nie kotek, ale kotkiem jest Filemon, kot, kot, kotek'))







