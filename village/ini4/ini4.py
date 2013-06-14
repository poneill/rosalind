#!/usr/bin/env python

import sys

"""
Problem

Given: Two positive integers a and b (a<b<10000).

Return: The sum of all odd integers from a through b, inclusively.

Sample Dataset

100 200

Sample Output

7500

"""

def odds(a,b):
    """Return odd integers from a to b inclusive"""
    return [i for i in range(a,b+1) if i % 2 == 1]
    
if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as f:
        a,b = map(int,f.readline().split(" "))
        print sum(odds(a,b))
