#!/usr/bin/env python
import sys
sys.path.append("..")
from rosalind_utils import *
"""
Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.
Sample Dataset

AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

Sample Output

MAMAPRTEINSTRING
"""

if __name__ == "__main__":
    seq = get_input()[0]
    print translate(seq)
