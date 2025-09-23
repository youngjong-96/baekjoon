# 최소비용 구하기

from heapq import heappop, heappush

import sys


def dijkstra(start_node):
    pque = [(0, start_node)]
    dists = [float('inf')] * (n + 1)
    dists[start_node] = 0

    while pque:
        dist, node = heappop(pque)

        if dists[node] < dist:
            continue

        for next_dist, next_node in graph[node]:
            new_dist = dist + next_dist

            if dists[next_node] <= new_dist:
                continue

            dists[next_node] = new_dist
            heappush(pque, (new_dist, next_node))

    return dists


n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().strip().split())
    graph[start].append((cost, end))

target_s, target_e = map(int, sys.stdin.readline().strip().split())

result = dijkstra(target_s)

print(result[target_e])