class Student:
    imie = None
    nazwisko = None

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

user1 = Student("Jan","Kowalski")
user2 = Student("Paweł","Racuch")
user3 = Student("Gaweł","Klusek")
user4 = Student("Michał","Kichał")

class Klasa:
    """użycie gettera"""
    lista_u = []
    __top_lista_u = 4 #maksymalna ilosc miejsc w klasie

    def add_student(self,student):
        if self.__top_lista_u > len(self.lista_u):
            if student not in self.lista_u:
                self.lista_u.append(student)
                return True
            else:
                return False
        else:
            raise KlassFullException("Brak wolnych miejsc w klasie")

    def remove_student(self, student):
        if student in self.lista_u:
            self.lista_u.remove(student)
            return True
        else:
            return False
    @property
    def klass_size(self):
        return len(self.lista_u)

    def clear(self):
        self.lista_u = []

    def is_in_class(self,student):
        if student in self.lista_u:
            return True
        else:
            return False
    @property
    def max_size(self):
        return self.__top_lista_u

class KlassFullException(Exception):
    pass

szkola = Klasa()
print(szkola.add_student(user1))
print(szkola.add_student(user2))
print(szkola.add_student(user3))
print(szkola.add_student(user3))
print(szkola.remove_student(user1))
print(szkola.remove_student(user4))
print(szkola.klass_size)
# szkola.clear()
# print(szkola.klass_size)
print(szkola.is_in_class(user2))
print(szkola.is_in_class(user4))

