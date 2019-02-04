"""
🌩Dreamy-Jy🌩 back at it again ⚡️...

Daily Coding Problem: Problem #10

Implement a job scheduler which takes in a function f and 
an integer n, and calls f after n milliseconds.
"""

import time


def schedule(job, wait):

    time.sleep(wait/1000)
    return job()
