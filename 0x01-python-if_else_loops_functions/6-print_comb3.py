#!/usr/bin/python3
for i in range(10):
    for j in range(1, 10):
        if i != j and j > i:
            print("{}{}, ".format(i, j), end="")
        elif i == j and j == 9:
            print("{}{}".format(i, j))
