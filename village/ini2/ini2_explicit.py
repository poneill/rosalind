#!/usr/bin/env python
import sys

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as f:
        line = f.readline()
    a_str,b_str = line.split(" ")
    a = int(a_str)
    b = int(b_str)
    print a**2 + b**2
