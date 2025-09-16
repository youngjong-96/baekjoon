# 최소 힙

import sys
from heapq import heappop, heappush

pq = []
n = int(sys.stdin.readline().strip())

for _ in range(n):
    x = int(sys.stdin.readline().strip())

    if x > 0:
        heappush(pq, x)
    else:
        if pq:
            print(heappop(pq))
        else:
            print(0)
