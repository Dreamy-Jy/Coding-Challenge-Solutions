'''
🌩Dreamy-Jy🌩 back at it again ⚡️...

Daily Coding Problem: Problem #4

Given an array of integers, find the first missing 
positive integer in linear time and constant space. 
In other words, find the lowest positive integer that 
does not exist in the array. The array can contain 
duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2.
The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''


def sorted_solution(seq):
    seq = sorted(seq)
    missing_number = 1

    for val in seq:
        if val > 0 and val == missing_number:
            missing_number += 1
        elif val > 0:
            return missing_number

    return missing_number


def unsorted_solution(seq):
    pass
