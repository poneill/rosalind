#!/usr/bin/env python
import sys

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as f:
        text_line, text_indices_line = f.readlines()
        text_indices = text_indices_line.split(" ")
        a,b,c,d = map(int,text_indices)
    print text_line[a:b+1], text_line[c:d+1]
