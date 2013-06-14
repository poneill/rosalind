#!/usr/bin/env python

"""
Reading and Writing

Problem

Given: A file containing at most 1000 lines.

Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

Sample Dataset

`Bravely bold Sir Robin rode forth from Camelot
Yes, brave Sir Robin turned about
He was not afraid to die, O brave Sir Robin
And gallantly he chickened out
He was not at all afraid to be killed in nasty ways
Bravely talking to his feet
Brave, brave, brave, brave Sir Robin
He beat a very brave retreat

Sample Output

Yes, brave Sir Robin turned about
And gallantly he chickened out
Bravely talking to his feet
He beat a very brave retreat
"""

import sys

def even_numbered_lines(lines):
    return [line for (i,line) in enumerate(lines) if i % 2 == 1]

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()
    out_lines = even_numbered_lines(lines)
    with open("rosalind_ini5.out",'w') as g:
        for line in out_lines:
            g.write(line)
        
    
