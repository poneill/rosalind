#!/usr/bin/env python
"""
Problem

Given: A string s of length at most 200 letters and four integers a, b, c and d.

Return: The slice of this string from indices a through b and c
through d (with space in between), inclusively.  Sample Dataset

HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
22 27 97 102

Sample Output

Humpty Dumpty

"""


import sys

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as f:
        text_line, text_indices_line = f.readlines()
        text_indices = text_indices_line.split(" ")
        a,b,c,d = map(int,text_indices)
    print text_line[a:b+1], text_line[c:d+1]
