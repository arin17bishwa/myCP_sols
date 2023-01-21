#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
D={'(':')','{':'}','[':']'}
DD={')':'(','}':'{',']':'['}
# Complete the isBalanced function below.
def isBalanced(s):
    de=deque([])
    for i in s:
        if len(de)==0:
            if (i in DD):return 'NO'
            de.append(i)
            continue
        if i in DD:
            if  DD[i]!=de[-1]:return 'NO'
            _=de.pop()
        else:de.append(i)
    if len(de)>0:return 'NO'
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
