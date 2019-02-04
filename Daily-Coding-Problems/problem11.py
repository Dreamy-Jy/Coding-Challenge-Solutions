"""
🌩Dreamy-Jy🌩 back at it again ⚡️...

Daily Coding Problem: Problem #11

Implement an autocomplete system. That is, given a query string s and a
set of all possible query strings, return all strings in the set that
have s as a prefix.

For example, given the query string de and the set of strings [dog, deer,
deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure
to speed up queries.
"""


# what if typed lomger than word
def iterative_solution(typed, words):
    return list(filter(lambda word: checkword(typed, word), words))


def checkword(typed, word):
    for i in range(len(typed)):
        if typed[i] != word[i]:
            return False
    return True


def checkword_closure(typed):
    def inner_checkword(word):
        for i in range(len(typed)):
            if typed[i] != word[i]:
                return False
        return True

    return inner_checkword


def regex_solution(typed, words):
    pass
