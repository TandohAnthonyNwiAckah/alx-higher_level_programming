#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    for i in range(0, x):
        try:
            my_list[i]
        except IndexError:
            print(end='')
        else:
            num += 1
            print(my_list[i], end='')
    print()
    return num
