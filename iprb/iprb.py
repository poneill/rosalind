#!/usr/bin/env python
import sys
sys.path.append("..")
from rosalind_utils import *
"""
Given: Three positive integers k, m, and n, representing a population
containing k+m+n organisms: k individuals are homozygous dominant for
a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms
will produce an individual possessing a dominant allele (and thus
displaying the dominant phenotype). Assume that any two organisms can
mate.

Sample Dataset

2 2 2

Sample Output

0.78333

"""

if __name__ == "__main__":
    k,m,n = map(int,get_input()[0].split(" "))
    total = float(sum([k,m,n]))
    AA_AA_prob = choose(k,2) * choose(m,0) * choose(n,0) / choose(total,2)
    AA_Aa_prob = choose(k,1) * choose(m,1) * choose(n,0) / choose(total,2)
    AA_aa_prob = choose(k,1) * choose(m,0) * choose(n,1) / choose(total,2)
    Aa_Aa_prob = choose(k,0) * choose(m,2) * choose(n,0) / choose(total,2)
    Aa_aa_prob = choose(k,0) * choose(m,1) * choose(n,1) / choose(total,2)
    dom_prob = (1.0   * AA_AA_prob +
                1.0   * AA_Aa_prob +
                1.0   * AA_aa_prob +
                3/4.0 * Aa_Aa_prob + 
                1/2.0 * Aa_aa_prob)
    print dom_prob
