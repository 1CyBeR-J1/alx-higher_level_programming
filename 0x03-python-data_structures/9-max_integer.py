#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maxlist = mylist[0]
    for i in my_list:
        if i > maxlist:
            maxlist = i
    return maxlist
