''' import os

while True:
    os.system("cls")
    s = input("계산식 입력>")
    print("결과: {}".format(eval(s)))
    os.system("pause")

'''

import os
operator = ["+", "-", "*", "/", "="]


def string_calculator(user_input, show_history=False):
    string_list = []
    lop = 0

    if user_input[-1] not in operator:
        user_input = "="

    for i, s in enumerate(user_input):
        if s in operator:
            if user_input[lop:i].strip() != "":
                string_list.append(user_input[lop:i])
                string_list.append(s)
                lop = i + 1
