"""
NOTE I didn't solve this problem.

🌩Dreamy-Jy🌩 back at it again ⚡️...

Daily Coding Problem: Problem #9

Given a list of integers, write a function that returns 
the largest sum of non-adjacent numbers. Numbers can be 
0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 
2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5
and 5.

Follow-up: Can you do this in O(N) time and constant space?

"""


# NOTE: not my solution, from Geeks for geeks
def dynamic_solution(seq):
    incl = 0
    excl = 0

    for val in seq:
        new_excl = excl if excl > incl else incl
        print("excl :"+str(excl))
        print("incl :"+str(incl)+"\n")
        incl = excl + val
        excl = new_excl

    print("excl :"+str(excl))
    print("incl :"+str(incl)+"\n")
    return (excl if excl > incl else incl)


def funcname(parameter_list):
    pass
