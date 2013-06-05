#!/usr/bin/env python
import sys
sys.path.append("..")
from rosalind_utils import *


if __name__ == "__main__":
    s,t = get_input()
    print hamming(s,t)
