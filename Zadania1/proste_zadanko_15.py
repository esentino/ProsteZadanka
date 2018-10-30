def dividers(number):
    if isinstance(number, int) and number > 0:
        dzielniki = []
        for i in range(1, number + 1):
            if number % i == 0:
                dzielniki.append(i)

        return dzielniki

    else:
        return


print(dividers(24))
print(dividers(0))
print(dividers(120))
