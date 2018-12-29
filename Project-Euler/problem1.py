"""
Problem 1: Multiples of 3 and 5

Find the sum of all number that multiples of
3 and 5 between 0 and 1000 exclusive.
"""


def brute_force(below):
    """

    """
    if type(below) is not int:
        raise TypeError(
            "the 'below' parameter of the brute_force() function must be of type int()")

    if below < 0:
        raise ValueError(
            "the 'below' parameter of the brute_force() function must be NON-negative")

    sum = 0

    for num in range(below):
        if num % 3 == 0 or num % 5 == 0:
            sum += num

    return sum


"""
another possible solution: 
sum([ num for num in range(below) if num %3 ==0 or num %5 ==0]) 

How do these solutions preform differently?
"""


def series_solution(below):
    if type(below) is not int:
        raise TypeError(
            "the 'below' parameter of the brute_force() function must be of type int()")

    if below < 0:
        raise ValueError(
            "the 'below' parameter of the brute_force() function must be NON-negative")

    sum3 = sum_series(below, 3)
    sum5 = sum_series(below, 5)
    sum15 = sum_series(below, 15)

    return sum3 + sum5 - sum15


def sum_series(end, common_difference):
    n = end // common_difference

    if end % common_difference == 0:
        n -= 1  # there's a possiblity of a negative n

    nth_term = common_difference + ((n - 1) * common_difference)

    return (n * (common_difference + nth_term)) // 2


if __name__ == "__main__":
    print(series_solution)
