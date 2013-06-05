#!/usr/bin/env python

"""
For a collection of strings and a positive integer k, the overlap
graph for the strings is a directed graph Ok in which each string is
represented by a node, and string s is connected to string t with a
directed edge when there is a length k suffix of s that matches a
length k prefix of t, as long as s!=t; we demand s!=t to prevent
directed loops in the overlap graph (although directed cycles may be
present).

Given: A collection of DNA strings in FASTA format having total length
at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges
in any order.

Sample Dataset

>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG

Sample Output

Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323
"""

import sys
sys.path.append("..")
from rosalind_utils import *

def edge(named_seq1,named_seq2,k):
    """If a length k suffix of 1 matches a length k prefix of two,
    there should be an edge from 1 to 2"""
    s,t = named_seq1[1],named_seq2[1]
    return (s != t) and (s[-k:] == t[:k])

def overlap_graph(named_seqs,k):
    return [(named_seq_i[0],named_seq_j[0])
            for named_seq_i in named_seqs
            for named_seq_j in named_seqs
            if edge(named_seq_i,named_seq_j,k)]

if __name__ == "__main__":
    named_seqs = parse_fasta_file(sys.argv[1])
    adj_list = overlap_graph(named_seqs,3)
    for row in adj_list:
 	print " ".join(row)
