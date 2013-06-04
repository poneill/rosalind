#!/usr/bin/env python
import sys

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as f:
        line = f.readline()
        a,b = map(int,line.split(" "))
    print a**2 + b**2
