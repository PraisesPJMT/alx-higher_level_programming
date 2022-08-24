#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_gigit = number % 10
print(f"Last digit of {number} is {last_gigit} ", end="")
if last_gigit > 5:
    print("and is greater than 5")
elif last_gigit == 0:
    print("and is 0")
elif (last_gigit > 0) and (6 > last_gigit):
    print("and is less than 6 and not 0")
