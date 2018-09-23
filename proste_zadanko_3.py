from numbers import Number


def speed(distance, time):
    result = 0
    if isinstance(distance, Number) and isinstance(time, Number):
        result = distance / time
        if int(result) == result:
            return "{0:.0f}".format(result)
        else:
            return result
    else:
        return "Podaj wartości liczbowe"


print(speed(100, 10))
print(speed(58, 12))
print(speed(90, 10))
print(speed(14, 2))
print(speed(15, 5))
print(speed(2, 2))
print(speed(144, 12))
print(speed(3, 6))
