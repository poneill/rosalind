#!/usr/bin/env python
"""
Given: A collection of at most 10 DNA strings of equal length (at most
1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If
several possible consensus strings exist, then you may return any one
of them.)
Sample Dataset

>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT

Sample Output

ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
"""

import sys
sys.path.append("..")
from rosalind_utils import *


if __name__ == "__main__":
    seqs = [seq for name,seq in parse_fasta_file(sys.argv[1])]
    cols = transpose(seqs)
    counts = [[col.count(b) for b in "ACGT"] for col in cols]
    row_counts = transpose(counts)
    cons_seq = consensus(seqs)
    print cons_seq
    for b,row_count in zip("ACGT",row_counts):
        print "%s:" % b, " ".join(map(str,row_count))
