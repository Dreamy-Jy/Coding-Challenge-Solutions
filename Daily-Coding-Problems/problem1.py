'''
🌩Dreamy-Jy🌩 back at it again ⚡️...

Daily Coding Problem: Problem #1

Given a list of numbers and a number k, return
whether any two numbers from the list add up to
k.

For example, given [10, 15, 3, 7] and k of 17,
return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''
from typing import List


def brute_force(seq: List[int], goal_sum: int) -> bool:
    """
    Using the brute force method, this function returns 
    a boolean representing whiether or not a list of `int`
    values, the `seq` parameter, contains at least one pair of values that
    sum to `goal_sum`.
    """
    if type(seq) is not list:
        raise TypeError("`seq` must be a `list` of `int` values.")

    for element in seq:
        if type(element) is not int:
            raise TypeError("All elements of `seq` must be `int` values.")

    if type(goal_sum) is not int:
        raise TypeError("`goal_sum` must be of type `int`.")

    for addend_one in range(len(seq)):
        addend_two: int = goal_sum - seq[addend_one]

        for possible_addend_two in range(addend_one + 1, len(seq)):
            if seq[possible_addend_two] == addend_two:
                return True

    return False


# TODO reword the function description
# TODO implement this function
def one_pass_solution(seq: List[int], goal_sum: int) -> bool:
    """
    In a single pass of the list `seq` this function returns 
    a boolean representing whiether or not a list of `int`
    values, the `seq` parameter, contains at least one pair of values that
    sum to `goal_sum`.
    """
    if type(seq) is not list:
        raise TypeError("`seq` must be a `list` of `int` values.")

    for element in seq:
        if type(element) is not int:
            raise TypeError("All elements of `seq` must be `int` values.")

    if type(goal_sum) is not int:
        raise TypeError("`goal_sum` must be of type `int`.")
