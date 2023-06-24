import exercise6


def count_all_characters(text):
    """
    Counts the occurrences of each character in a string and returns a dictionary.

    Args:
        text: The string to analyze.

    Returns:
        A dictionary with characters as keys and their occurrence counts as values.
    """

    output = {}

    for character in text:
        if character.isalpha():
            output[character] = exercise6.count_character(text, character)

    return output


result = count_all_characters('Mam dzisiaj dobry humor')

#  join łączy elementy słownika, separator nowa linia
#  items() zwraca parę klucz-wartość dla każdego elementu słownika
print("\n".join(f"{key}: {value}" for key, value in result.items()))
