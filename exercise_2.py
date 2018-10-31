def min_and_max(lista):
    if not lista: #sprawdzenie pustej listy
        return None, None
    else:
        nw = max(lista)
        nm = min(lista)
        return nm , nw
# #Napisz funkcję min_and_max(lista), która przyjmuję listę liczb a zwraca krotkę z najmniejszą i największą liczbą z listy
# #
# print(min_and_max([3,5,-3,12,-2,0])) # zwróci (-3, 12)
#
# print(min_and_max([12])) # zwróci (12,12)
#
# print(min_and_max([])) # zwróci (None, None)