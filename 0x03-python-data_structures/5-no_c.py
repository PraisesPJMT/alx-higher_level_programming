#!/usr/bin/python3
def no_c(my_string):
    my_new_string = ''
    for char in my_string:
        if char is not 'c' and char is not 'C':
            my_new_string += char
    return my_new_string
