#!/usr/bin/env python
"""mapper.py"""

import sys
topwords = ["football","real","team","madrid","game","match","win","one","first","play"]
tempWord = ""
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    for topword in topwords:
        for i in range(0, len(words)-1):
            if words[i] == topword:
                print("%s|%s\t%s" % (words[i],words[i+1], 1))