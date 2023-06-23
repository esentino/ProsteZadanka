def count_character(text, letter):
    """
    Counts the number of times a character appears in a string.

    Args:
        text: The string to search.
        letter: The character to count.

    Returns:
        The number of times the character appears in the string.
    """
    text = text.lower()
    letter = letter.lower()

    return text.count(letter)


# print(count_character('Mam dzisiaj dobry humor', 'm'))
# zwróci 3
