class Klasa:
    lista_u = []

    def add_student(self,student):
        if student not in self.lista_u:
            self.lista_u.append(student)
            return True
        else:
            return False

    def remove_student(self, student):
        if student in self.lista_u:
            self.lista_u.remove(student)
            return True
        else:
            return False

    def klass_size(self):
        return len(self.lista_u)

    def clear(self):
        self.lista_u = []

    def is_in_class(self,student):
        if student in self.lista_u:
            return True
        else:
            return False


szkola = Klasa()
szkola.add_student("michał")
szkola.add_student("kuba")
szkola.add_student("jola")
print(szkola.klass_size())
print(szkola.is_in_class("michał"))
print(szkola.is_in_class("natalia"))
szkola.remove_student("kuba")
print(szkola.klass_size())
szkola.add_student("piotrek")
print(szkola.is_in_class("piotrek"))
szkola.clear()
print(szkola.klass_size())


