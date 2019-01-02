"""
Problem 2: Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by
adding the previous two terms. By starting with 1 and 2,
the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose
values do not exceed four million, find the sum of the
even-valued terms.
"""
import math

# TODO Make the outputs of brute_force() and fibonacci_formula_solution() equal


def brute_force(limit: int) -> int:
    fib_seq = [0, 1]
    seq_end = len(fib_seq) - 1
    fib_sum = 0

    # generate the fibonacci sequence that ends in a
    # number greater than or equal to the 'limit' parameter
    while fib_seq[seq_end] < limit:
        fib_seq.append(
            fib_seq[seq_end] + fib_seq[seq_end - 1])
        seq_end = len(fib_seq) - 1

    # Removes unnesscary values from the list
    # TODO Make this more efficent with pops
    fib_seq = fib_seq[2:len(fib_seq) - 1]

    # sum all the even numbers in the list
    for num in fib_seq:
        if num % 2 == 0:
            fib_sum += num

    return fib_sum


# NOTE Untested
def fibonacci_formula_solution(limit: int)->int:
    if limit < 2:
        return 0

    fib_sum = 2
    fib = 2
    n = 3

    # TODO refactor this loop, that if is unacceptable.
    while fib < limit:
        n += 3
        fib = calculate_fibonacci_at(n)

        if fib > limit:
            return fib_sum

        fib_sum += fib

    return fib_sum


# NOTE Untested
def calculate_fibonacci_at(n: int) -> int:
    '''Calculates the fiboncci number at `n`, using the fibonacci formula.'''
    𝛷: float = (1 + math.sqrt(5)) / 2

    𝜑: float = (1 - math.sqrt(5)) / 2

    return int((math.pow(𝛷, n) - math.pow(𝜑, n)) / math.sqrt(5))
