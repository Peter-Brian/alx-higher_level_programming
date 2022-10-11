#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    run, num = 0, 0
    while run < x:
        try:
            print("{:d}".format(my_list[run]), end='')
            num += 1
        except (ValueError, TypeError):
            pass
        run += 1
    print()
    return num
