import abc


def solution(password):
    length = len(password)
    for i in range(length - 2):
        first_check = ord(password[i+1]) - ord(password[i])
        second_check = ord(password[i]) - ord(password[i+1])
        if first_check == second_check and (first_check == 1 or first_check == -1):
            return False
    return True

    passsword1 = "cospro890"

    length = 9

    first_check = o - c
    second_check = s - o


abc
b-a
c-b
