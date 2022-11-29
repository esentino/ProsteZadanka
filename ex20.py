def is_surname_correct():
    try:
        s = str(input("Podaj nazwisko: "))
        l = len(s)
        if s[0].islower() or s.find(' ')!=-1 or l<4:
            raise ValueError
    finally:
        print("Poprawne nazwisko")


is_surname_correct()

# Napisz funkcję do sprawdzania poprawności nazwiska:
#
# poprawne nazwisko ma conajmniej 3 litery
# nazwisko zaczyna się z dużej litery
# w nazwisku nie występuje spacja
