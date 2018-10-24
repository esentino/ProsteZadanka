# Proste zadanka2

1. Napisz klase `Uzyszkodnik`, która będzie reprezentować użytkownika naszej aplikacji z następującymi opcjami:
    1. imię użytkownika - tekstowe max 32 znaki i musi się zaczynać od dużej litery
    2. nazwisko użytkownika - tekstowe max 64 znaki i musi się zaczynać od dużej litery
    3. wiek użytkownika - liczbowe (od 18 do 99 lat)
    4. staż użytkownika - liczbowe (ile dni ma konto w naszej aplikacji)
    5. dynamiczną właściwość zwracającą imię i nazwisko jako jeden string
    6. metodę `rabat(product_price)`, która zwróci kwotę rabatu o jaką zostanie pomniejszona cena produktu (rabat jest procentowy i wyliczany jako staż użytkownika)

2. Napisz klasę `Student`, która ma następujące właściwości:
    1. imię
    2. nazwisko
    3. konstrutor przyjmujacy imię i nazwisko ucznia

3. Klasę `Klasa`, która będzie miała następujące właściwości:
    1. liste uczniow - lista przechowująca obiekty klasy student
    2. metodę `add_student(student)`, która doda ucznia do listy uczniów jeśli nie ma jego w niej (zwróci `True` w przeciwnym wypadku `False`)
    3. metodę `remove_student(student)`,  która usunię ucznia z listy uczniów (zwróci `True` jeśli został usunięty, `False` jeśli nie było go na liście)
    4. metodę `klass_size()`, która zwróci liczbę uczniów w klasie
    5. metodę `clear()`, która wyczyści listę uczniów
    6. metodę `is_in_klass(student)`, sprawdza czy podany student jest w klasie

4. Zmodyfikuj klasę `Klasa`, tak aby:
    1. miała właściwość `max_size` - maksymalną liczbę uczniów jaką pomieści klasa
    2. zmodyfikuje metodę `add_student(student)`, aby w przypadku próby dodania ucznia do pełnej klasy rzuciła wyjątkiem `KlassFullException`([przykład](#jak-napisać-własny-wyjątek)).

## Tipsy i inne dodatki do paznokci.

### Jak napisać własny wyjątek

```py
        ```py
        class KlassFullException(Exception):
            pass
        ```
