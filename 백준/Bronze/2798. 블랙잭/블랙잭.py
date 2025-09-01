# 블랙잭

import sys, itertools


n, m = map(int, sys.stdin.readline().strip().split())

numbers = list(map(int, sys.stdin.readline().strip().split()))


pos = list(itertools.combinations(numbers, 3))

result = 0

for p in pos:
    if sum(p) <= m:
        if sum(p) > result:
            result = sum(p)

print(result)