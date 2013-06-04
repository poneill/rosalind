#!/usr/bin/env python

"""
Given: Positive integers n<=40 and k<=5.
Return: The total number of rabbit pairs that will be present after n
months if each pair of reproduction-age rabbits produces a litter of k
rabbit pairs in each generation (instead of only 1 pair).  Sample
Dataset

5 3

Sample Output

19
"""

def get_input():
    import sys
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()
    return lines

def fib(n,k):
    if n <3:
        return 1
    else:
        return fib(n - 1,k) + k*fib(n - 2,k)

if __name__ == "__main__":
    n,k = map(int,get_input()[0].split(" "))
    print fib(n,k)
