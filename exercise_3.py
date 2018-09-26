def speed(distance,time):
    if distance >= time:
        wynik = str(int(distance / time)) , "m\s"
    else:
        wynik = str(distance / time), "m\s"
    wynik = " ".join(wynik)
    return wynik

# print(speed(100,10) ) # zwróci 10 m/s
# print(speed(2,10) ) # zwróci 10 m/s