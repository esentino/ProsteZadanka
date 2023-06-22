def multiply_list(lista, num):
    """
    Multiplies each element of a list by a given number and returns a new list.

    Args:
        lista (list): A list of numbers to multiply.
        num (int): A number to multiply the list elements by.

    Returns:
        list: A list of the multiplication results.

    """
    return [elem * num for elem in lista]


print(multiply_list([3, 5, 2, 6], 2))
# zwróci [6,10,4,12]
