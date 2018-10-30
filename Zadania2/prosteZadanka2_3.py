class Student:
    first_name = None
    last_name = None

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Klasa:
    student_list = []

    def add_student(self, student):
        if student not in self.student_list:
            self.student_list.append(student)
            return True
        else:
            return False

    def remove_student(self, student):
        if student in self.student_list:
            index = self.student_list.index(student)
            self.student_list.pop(index)
            return True
        else:
            return False

    def klass_size(self):
        return len(self.student_list)

    def clear(self):
        self.student_list = []

    def is_in_klass(self, student):
        return student in self.student_list


if __name__ == '__main__':
    student1 = Student("Jerzy", "Ryba")
    student2 = Student("Stefan", "Siarzewski")
    student3 = Student("Jurek", "Kiler")
    student4 = Student("Gabrysia", "Siarzewska")
    student5 = Student("Ferdynand", "Lipski")

    klasa1 = Klasa()
    klasa2 = Klasa()

    klasa1.add_student(student1)
    klasa1.add_student(student2)
    klasa1.add_student(student3)

    print(klasa1.is_in_klass(student4))
    print(klasa1.klass_size())

    for uczen in klasa1.student_list:
        print(uczen.first_name, uczen.last_name)

    print("\nCzyszczenie listy uczniów.")
    klasa1.clear()

    for entity in klasa1.student_list:
        print(entity.first_name, entity.last_name)

