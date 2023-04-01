#!/usr/bin/env python
"""mapper.py"""

import sys

total = 0
count = 0

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    values = list(map(int, line.strip().split()))
    # increase counters
    for value in values:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        print(f"{value}\t1")

        

