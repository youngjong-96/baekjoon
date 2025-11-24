import sys
from collections import deque


def bfs(start):
    global plane_cnt

    que = deque([start])

    while que:
        t = que.popleft()
        for next_node in graph[t]:
            if not visited_n[next_node]:
                visited_n[next_node] = 1
                plane_cnt += 1
                que.append(next_node)

T = int(sys.stdin.readline().strip())
for _ in range(T):
    nation, plane = map(int, sys.stdin.readline().strip().split())
    # [[1, 2], [0, 2], [1, 0]]
    graph = [[] for _ in range(nation)]

    for i in range(plane):
        s, e = map(int, sys.stdin.readline().strip().split())
        graph[s-1].append(e-1)
        graph[e-1].append(s-1)

    visited_n = [0] * nation
    plane_cnt = 0

    for i in range(nation):
        if visited_n[i]:
            continue
        visited_n[i] = 1
        bfs(i)

    print(plane_cnt)