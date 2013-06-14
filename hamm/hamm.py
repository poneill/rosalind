#!/usr/bin/env python
import sys
sys.path.append("..")
from rosalind_utils import *

"""
Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
Sample Dataset

GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT

Sample Output

7
"""

if __name__ == "__main__":
    s,t = get_input()
    print hamming(s,t) 
