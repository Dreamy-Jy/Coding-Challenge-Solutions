from sys import maxsize
"""
🌩Dreamy-Jy🌩 back at it again ⚡️...

Daily Coding Problem: Problem #49

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.


"""


def brute_force(seq):
    sums = seq.copy()
    sums.append(sum(seq))

    for sub_array_len in range(2, len(seq)):
        for i in range(len(seq) - sub_array_len + 1):
            sums.append(sum(seq[i:i + sub_array_len]))

    max_sum = max(sums)
    return max_sum if max_sum >= 0 else 0


def kadane_solution(seq):
    """ 
    This solution is not my own, and can be found here 
    https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
    (It doesn't work)
    """

    max_so_far = -maxsize
    max_ending_here = 0

    for val in seq:
        max_ending_here = max_so_far + val

        if max_ending_here < 0:
            max_ending_here = 0
        elif max_so_far < max_ending_here:
            max_so_far = max_ending_here

    return max_so_far


if __name__ == "__main__":
    print(brute_force([34, -50, 42, 14, -5, 86]))
    print(brute_force([-5, -1, -8, -9]))
    print(brute_force([-2, -3, 4, -1, -2, 1, 5, -3]))
    print()
    print(kadane_solution([34, -50, 42, 14, -5, 86]))
    print(kadane_solution([-5, -1, -8, -9]))
    print(kadane_solution([-2, -3, 4, -1, -2, 1, 5, -3]))
