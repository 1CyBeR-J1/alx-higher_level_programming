#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newlist = []
    for i in my_list:
        if i % 2 == 0:
            i = True
        else:
            i = False
    return newlist
