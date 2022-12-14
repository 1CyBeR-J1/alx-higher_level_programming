#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    ints = list(map(lambda x: roman.get(x, 0), roman_string))
    length = len(ints)
    for i in range(length):
        if i + 1 < length:
            if ints[i] < ints[i + 1]:
                ints[i] = -ints[i]
    return sum(ints)
