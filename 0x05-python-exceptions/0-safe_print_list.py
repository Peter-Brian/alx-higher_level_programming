#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    run = 0
    try:
        while run in range(x):
            print(my_list[run], end='')
            run += 1
    except IndexError:
        None
    print()
    return(run)
