#!/usr/bin/env python
import sys
sys.path.append("..")
from rosalind_utils import *

def gc(seq):
    n = len(seq)
    c_counts = seq.count("C")
    g_counts = seq.count("G")
    return (c_counts + g_counts)/float(n)

if __name__ == "__main__":
    seqs = parse_fasta_file(sys.argv[1])
    best_name,best_seq = max(seqs,key=lambda (name,seq):gc(seq))
    best_gc_content = gc(best_seq)
    print best_name
    print best_gc_content * 100
    
    
