#!/usr/bin/env python

"""
In DNA strings, symbols 'A' and 'T' are complements of each other, as
are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by
reversing the symbols of s, then taking the complement of each symbol
(e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
Sample Dataset

AAAACCCGGT

Sample Output

ACCGGGTTTT
"""

def get_input():
    import sys
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()
    return lines

def revc(seq):
    comp = {"A":"T","C":"G","G":"C","T":"A"}
    return "".join([comp[b] for b in seq])[::-1]

if __name__ == "__main__":
    seq = get_input()[0].strip()
    print revc(seq)
    
