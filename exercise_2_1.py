class Uzyszkodnik:
    imie = None
    nazwisko = None
    wiek = None
    staz = None

    def __init__(self, imie, nazwisko, wiek, staz):
        if isinstance(imie,str) and len(imie) <= 32 and imie[0].isupper():
            self.imie = imie
        else:
            raise ValueError("Podaj imie w formacie string, zaczynające się z dużej litery, Imię nie może być dluższe niż 32 znaki")
        if isinstance(nazwisko, str) and len(nazwisko) <= 64 and nazwisko[0].isupper():
            self.nazwisko = nazwisko
        else:
            raise ValueError("Podaj nazwisko w formacie string, zaczynające się z dużej litery, nazwisko nie może być dluższe niż 64 znaki")
        if isinstance(wiek,int) and wiek >= 18 and wiek <= 99:
            self.wiek = wiek
        else:
            raise ValueError("Podaj wiek jako liczbę całkowitą z zakresu 18-99")
        if isinstance(staz,int):
            self.staz = staz
        else:
            raise ValueError("Podaj staż jako liczbę całkowitą")
        # print("{}-{}-{}-{}.".format(self.imie,self.nazwisko,self.wiek,self.staz))

    def rabat(self,product_price):
        return (self.staz / 100) * product_price

    @property
    def imie_nazw_razem(self):
        return ("{} {}".format(self.imie,self.nazwisko))

user1 = Uzyszkodnik("Jan","Kowalski", 18, 15)
print(user1.rabat(45))
print(user1.imie_nazw_razem)

