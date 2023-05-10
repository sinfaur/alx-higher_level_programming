#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Function to print x elements of my_list"""

    idx = 0
    for idx in range(x):
        try:
            print(my_list[idx], end='')
            idx += 1
        except IndexError:
            break
    print()
    return idx
