class Student:
    imie = None
    nazwisko = None

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

user1 = Student("Jan","Kowalski")
