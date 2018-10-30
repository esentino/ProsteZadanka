def divide_or_not_divide(by, not_by, max):
    if (isinstance(i, int) for i in [by, not_by, max]) \
            and (by and not_by and max) >= 0:

        lista_robocza = []
        output = "0 "  # dodaję sztywno, bo zero jest podzielne przez wszystko

        for i in range(max + 1):
            if i % by == 0 and i % not_by != 0:
                lista_robocza.append(i)

        for element in lista_robocza:
            output += str(element) + " "

        print(output)

    else:
        return "Podaj liczby naturalne jako parametry."


divide_or_not_divide(3, 4, 15)
divide_or_not_divide(2, 3, 13)
