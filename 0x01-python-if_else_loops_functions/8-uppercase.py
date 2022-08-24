#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            print("{:s}".format(chr(ord(i) - 32)), end='')
    print()
