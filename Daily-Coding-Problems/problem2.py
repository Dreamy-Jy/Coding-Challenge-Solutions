'''
Daily Coding Problem: Problem #2

Given an array of integers, return a new array
such that each element at index i of the new array
is the product of all the numbers in the original array
except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected
output would be [120, 60, 40, 30, 24]. If our input was
[3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''
from typing import List
from itertools import repeat


def brute_force(seq: List[int]) -> List[int]:
    pass


# TODO validate input
# TODO unit test
# TODO write function discription
def divison_solution(seq: List[int]) -> List[int]:
    seq_product = prod(seq)
    return list(map(remove_from_prod, seq, repeat(seq_product)))


# TODO validate input
# TODO unit test
# TODO write function discription
def prod(seq: List[int]) -> int:
    product = 1
    for val in seq:
        product *= val
    return product


# TODO validate input
# TODO unit test
# TODO write function discription
def remove_from_prod(element: int, prod: int) -> int:
    return prod // element
