#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list[idx] < 0 or mylist[idx] > (len(my_list) - 1):
        return my_list
    else:
        del my_list[idx]
