#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return 0
    x = y = 0
    for (score, weight) in my_list:
        x = sum(score * weight)
        y = sum(weight)
        return (x / y)
