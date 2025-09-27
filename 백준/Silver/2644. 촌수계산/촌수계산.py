# 촌수 계산

import sys
from collections import deque


def find_route(s):
    que = deque()
    visited = [0] * (n + 1)
    que.append(s)
    visited[s] = 1

    while que:
        t = que.popleft()
        for i in graph[t]:
            if visited[i]:
                continue
            visited[i] = visited[t] + 1
            que.append(i)

    return visited

n = int(sys.stdin.readline().strip())
ts, te = map(int, sys.stdin.readline().strip().split())
m = int(sys.stdin.readline().strip())

graph = [[] for _ in range(n + 1)]
for i in range(m):
    p, c = map(int, sys.stdin.readline().strip().split())
    graph[p].append(c)
    graph[c].append(p)

res = find_route(ts)
if res[te] == 0:
    print(-1)
else:
    print(res[te] - 1)
