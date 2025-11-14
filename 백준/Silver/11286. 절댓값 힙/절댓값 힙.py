import sys
from heapq import heappop, heappush

n = int(sys.stdin.readline().strip())
pq = []

for _ in range(n):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if pq:
            print(heappop(pq)[1])
        else:
            print(0)
    else:
        heappush(pq, (abs(x), x))