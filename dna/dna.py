#!/usr/bin/env python
"""
A string is simply an ordered collection of symbols selected from
some alphabet and formed into a word; the length of a string is the
number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the
symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective
number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
Sample Dataset

AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

Sample Output

20 12 17 21
"""

import sys

def mononucleotide_counts(seq):
    return {b:seq.count(b) for b in "ACGT"}

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as f:
        line = f.readline()
    counts = mononucleotide_counts(line)
    print " ".join(map(str,[counts[b] for b in "ACGT"]))
