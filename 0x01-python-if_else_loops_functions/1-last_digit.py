#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldigit = int(str(number)[-1])

if number < 0:
    ldigit = int(f"-{ldigit}")

if ldigit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, \
    ldigit))

elif ldigit == 0:
    print("Last digit of {} is {} and is 0".format(number, ldigit))

elif ldigit < 6 and ldigit != 0:
    print("Last digit of {} is {} and is less than 6 and not 0" \
    .format(number, ldigit))
