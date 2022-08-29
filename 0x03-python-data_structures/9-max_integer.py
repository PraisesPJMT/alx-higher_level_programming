#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    my_max_integer = my_list[0]
    for i in my_list:
        if i > my_max_integer:
            my_max_integer = i
    return my_max_integer
