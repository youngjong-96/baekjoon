# 트리의 부모 찾기

import sys
from collections import deque

def bfs(start_node):
    que = deque([start_node])
    visited = [0] * (n+1)
    visited[start_node] = 1

    data = [0] * (n+1)

    while que:
        parent = que.popleft()
        for child in graph[parent]:
            if not visited[child]:
                visited[child] = 1
                data[child] = parent
                que.append(child)

    return data


n = int(sys.stdin.readline().strip())
graph = [[] for _ in range(n + 1)]

for _ in range(n-1):
    s, e = map(int, sys.stdin.readline().strip().split())
    graph[s].append(e)
    graph[e].append(s)

data = bfs(1)

for i in range(2, n+1):
    print(data[i])