from numbers import Number


def diff_avg_medjana(lista):
    n = len(lista)

    try:
        lista.sort()  # jeśli wśród liczb jest string, rzuci TypeError
        if all(isinstance(item, Number) for item in lista):

            # obliczanie mediany
            if n % 2 == 0:
                val_1 = lista[int(n/2) - 1]  # indeksowanie od 0, dlatego odejmuję 1
                val_2 = lista[int(n/2)]      # a tu nie dodaję 1
                med = (val_1 + val_2)/2

            else:
                med = lista[int((n + 1)/2 - 1)]

            # obliczanie średniej
            avg = sum(lista)/len(lista)

        else:
            raise TypeError
    except TypeError:
        return "Przyjmuję tylko listę liczb"

    return round(abs(med - avg), 10)  # zaokrąglam do 10 miejsc po przecinku





lista1 = [2,4,4,2,5]
lista2 = [3,2,2,3,6,2]
lista3 = ['A','B','B','B','C']
lista4 = [3,2,2,'A','B','B',3,5,2]

x = diff_avg_medjana(lista1)
y = diff_avg_medjana(lista2)
z = diff_avg_medjana(lista3)
a = diff_avg_medjana(lista4)
print(x)
print(y)
print(z)
print(a)
