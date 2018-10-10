from collections import Counter

# wersja z biblioteką collections i metodą Counter
def count_character(text, letter):
    t=text.lower()
    count=Counter(t)
    r=count[letter]
    return r

# wersja bez biblioteki collections i funcji Counter
# def count_character(text, letter):
#     calc=0
#     for pos, c in enumerate(text):
#         if c == letter or c==letter.upper():
#             calc+=1
#     return calc

r1=count_character('Mam dzisiaj dobry humor', 'm')
print(r1)
# zwróci 3
