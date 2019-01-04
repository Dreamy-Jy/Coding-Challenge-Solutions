from string import ascii_uppercase
from re import match, findall


def iterative_solution(word: str) -> int:
    # Check for edge cases
    if len(word) == 0 or word == ' ':
        return 0

    # Count set to 1 too account for the first word
    word_count = 1

    # increment the count everytime a capital letter appears in the string
    for letter in word:
        if letter in ascii_uppercase:
            word_count += 1

    # return the word count with the addition of the original word.
    return word_count


def regex_solution(word: str) -> int:
    # initalize the count, with respect to the whiether
    # their is a starting lowercase letter
    word_count = 1 if match(r'^[a-z]', word) else 0

    # Uppercase letters represent words, so we add the
    # amount of them in the string to the count.
    word_count += len(findall(r'[A-Z]', word))
    return word_count
