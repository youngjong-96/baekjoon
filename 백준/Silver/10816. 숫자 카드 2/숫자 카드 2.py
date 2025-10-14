# 숫자카드 2

import sys

n = int(sys.stdin.readline().strip())
have = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
check = list(map(int, sys.stdin.readline().strip().split()))

visited = [0] * 20000001

for i in range(n):
    visited[have[i] + 10000000] += 1

for i in range(m):
    print(visited[check[i] + 10000000], end=' ')
