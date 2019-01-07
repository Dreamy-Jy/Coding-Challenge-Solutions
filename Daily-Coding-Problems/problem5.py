"""
🌩Dreamy-Jy🌩 back at it again ⚡️...

Daily Coding Problem: Problem #5

cons(a, b) constructs a pair, and car(pair) and cdr(pair)
returns the first and last element of that pair. For
example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4))
returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.

NOTE

This quest basically ask do you know functional programming
Which I don't yet.
"""


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    def get_first(a, b):
        return a

    return pair(get_first)


def cdr(pair):
    def get_second(a, b):
        return b

    return pair(get_second)
