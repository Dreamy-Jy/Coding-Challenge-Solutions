"""
🌩Dreamy-Jy🌩 back at it again ⚡️...

Hackerrank Strong Password problem
Problem Statement Can be found here: 
https://www.hackerrank.com/challenges/strong-password/problem
"""
from string import ascii_lowercase, ascii_uppercase, digits


def iterative_solution(password: str) -> int:

    special_characters = "!@#$%^&*()-+"

    fix_it_num = 0

    flag_sum = 0
    upper_case_flag = False
    lower_case_flag = False
    digit_flag = False
    special_char_flag = False

    for char in password:
        if upper_case_flag == False and char in ascii_uppercase:
            upper_case_flag = True
            flag_sum += 1
        elif lower_case_flag == False and char in ascii_lowercase:
            lower_case_flag = True
            flag_sum += 1
        elif digit_flag == False and char in digits:
            digit_flag = True
            flag_sum += 1
        elif special_char_flag == False and char in special_characters:
            special_char_flag = True
            flag_sum += 1

    if len(password) >= 6:
        return flag_sum

    if flag_sum > (6 - len(password)):
        return flag_sum

    return (6 - len(password))


def regex_solution(password: str) -> int:

    pass
