class KlassFullException(Exception):
    pass

class Klasa:
    lista_u = []
    top_lista_u = None

    def add_student(self,student):
        if self.top_lista_u > len(self.lista_u):
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
        return self.top_lista_u


szkola = Klasa()
szkola.top_lista_u = 2
szkola.add_student("michał")
szkola.add_student("kuba")
szkola.add_student("jola")
print(szkola.klass_size)
# print(szkola.klass_size())
# print(szkola.max_size)


