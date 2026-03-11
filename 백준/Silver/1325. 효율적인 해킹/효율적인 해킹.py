import sys
from collections import deque

input = sys.stdin.readline

def bfs(start_node):
    queue = deque([start_node])
    visited = [False] * (N + 1)
    visited[start_node] = True
    count = 1
    
    while queue:
        curr = queue.popleft()
        for neighbor in graph[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
    return count

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[e].append(s)

max_hack = -1
results = []

for i in range(1, N + 1):
    if graph[i]:  
        cnt = bfs(i)
        if cnt > max_hack:
            max_hack = cnt
            results = [i]
        elif cnt == max_hack:
            results.append(i)
    else:
        if max_hack < 1:
            max_hack = 1
            results = [i]
        elif max_hack == 1:
            results.append(i)

print(*(sorted(results)))