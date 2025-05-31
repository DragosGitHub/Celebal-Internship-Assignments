#!/bin/python3

import math
import os
import random
import re
import sys

# I am writing the required function here
def solve(s):
    # I am splitting the string into words and capitalizing each
    words = s.split(' ')
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

# Main code starts from here
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
