def sum_range(min, max):
    total = 0
    if isinstance(min, int) and isinstance(max, int):
        for i in range(min, max + 1):
            total += i
        return total
    else:
        return "Podaj liczby całkowite jako parametry funkcji"


print(sum_range(2, 5))
print(sum_range(-2, 2))
print(sum_range(0, 13))
print(sum_range(-100, 100))
print(sum_range(20, "Andrzej"))
print(sum_range(20, 3.5))
print(sum_range(30, complex(3, 5)))
