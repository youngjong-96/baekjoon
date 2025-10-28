from heapq import heappop, heappush
import sys

hq = []
n = int(sys.stdin.readline().strip())
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    if num == 0 and hq:
        print(-heappop(hq))
    elif num == 0 and not hq:
        print(0)
    else:
        heappush(hq, -num)