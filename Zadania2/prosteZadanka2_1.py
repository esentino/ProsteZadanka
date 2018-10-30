class Uzyszkodnik:

    def __init__(self, first_name, last_name, age, days):
        if isinstance(first_name, str) and first_name and len(first_name) <= 32 and first_name[0].isupper():
            self.first_name = first_name
        else:
            print("Imię musi się zaczynać z wielkiej litery i mieć co najwyżej 32 znaki.")

        if isinstance(last_name, str) and last_name and len(last_name) <= 64 and last_name[0].isupper():
            self.last_name = last_name
        else:
            print("Nazwisko musi się zaczynać z wielkiej litery i mieć co najwyżej 64 znaki.")

        if isinstance(age, int) and age and (18 <= age <= 99):
            self.age = age
        else:
            print("Wiek musi być liczbą całkowitą, w zakresie od 18 do 99 lat.")

        if isinstance(days, int) and days and days >= 0:
            self.days = days
        else:
            print("Liczba dni musi być całkowita i nie może być mniejsza niż 0.")

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    def rabat(self, product_price):
        return product_price * (self.days/10)/100  # 1% za każde 10 dni


if __name__ == '__main__':
    uzyszkodnik1 = Uzyszkodnik("Antoni", "Obroni", 87, 64)
    uzyszkodnik2 = Uzyszkodnik("Ambroży", "Przełoży", 54, 12)
    uzyszkodnik3 = Uzyszkodnik("Janek", "Dzbanek", 22, 120)
    uzyszkodnik4 = Uzyszkodnik("Paweł", "Gaweł", 45, 34)
    uzyszkodnik5 = Uzyszkodnik("Wujek", "Mujek", 18, 32)

    print(uzyszkodnik3.full_name)
    print(uzyszkodnik1.rabat(35))
