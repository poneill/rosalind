#!/usr/bin/env python
import sys

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as f:
        line = f.readline()
    fields = line.split(" ")
    a = int(fields[0])
    b = int(fields[1])
    print a**2 + b**2
