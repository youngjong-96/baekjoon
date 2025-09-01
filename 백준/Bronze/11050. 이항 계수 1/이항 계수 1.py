# 이항 계수

import sys, itertools

n, k = map(int, sys.stdin.readline().strip().split())

print(len(list(itertools.combinations(range(1, n+1), k))))