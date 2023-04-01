#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

total = 0
count = 0

# input comes from STDIN
for line in sys.stdin:
    value, count_str = line.strip().split('\t')
    count = count + int(count_str)
    total = total + int(value) * int(count_str)

print(f"{total/count}")
