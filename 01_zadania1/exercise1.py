def sum_range(min, max):
    if not isinstance(min, int) or  not isinstance(max, int):
        return "min and max must be integers"

    if min > max:
        return "min must be less than or equal to max"

    return sum(range(min, max + 1))


print(sum_range(2, 5))  # 14

print(sum_range(-2, 2))  # 0
