#!/usr/bin/env python
from rosalind_utils import *

"""
Our aim is to somehow modify this recurrence relation to achieve a
dynamic programming solution in the case that all rabbits die out
after a fixed number of months. See Figure 4 for a depiction of a
rabbit tree in which rabbits live for three months (meaning that they
reproduce only twice before dying).

Given: Positive integers n<=100 and m<=20.

Return: The total number of pairs of rabbits that will remain after
the n-th month (n<=100) if all rabbits live for m months (m<=20).
Sample Dataset
"""

def fibd(n,m):
    pop = [1] + [0]*(m-1)
    for i in range(n-1):
        pop = [sum(pop[1:])] + pop[:-1]
    return sum(pop)

if __name__ == "__main__":
    n,m = map(int,get_input()[0].split())
    print fibd(n,m)
