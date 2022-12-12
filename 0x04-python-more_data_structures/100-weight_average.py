#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    for score, weight in my_list:
        x = sum(score * weight)
        y = sum(weight)
        return (x / y)
