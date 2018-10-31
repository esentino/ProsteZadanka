def validate_name(nazwisko):
    try:
        if len(nazwisko) < 3 :
            raise ValueError(" Za krótkie nazwisko")
        first_letter = nazwisko[0]
        if first_letter.islower():
            raise ValueError(" Nazwisko powinno być z dużej litery")
        if " " in nazwisko:
            raise ValueError(" W nazwisku nie może być spacji")
        else:
            return True
    except ValueError as e:
        print("Błąd: {}".format(e))

# print(validate_name("Ko"))
# print(validate_name("kowalski"))
# print(validate_name("Ko walski"))
# print(validate_name("Kowalski"))
