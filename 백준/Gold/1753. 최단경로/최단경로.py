import sys
from heapq import heappop, heappush

input = sys.stdin.readline

V, E = map(int, input().split())
start_node = int(input().strip())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start].append((weight, end))

def dijkstra(start):
    pq = [(0, start)]
    dists = [200001] * (V + 1)
    dists[start] = 0

    while pq:
        dist, node = heappop(pq)

        if dists[node] < dist:
            continue

        for next_dist, next_node in graph[node]:
            new_dist = dist + next_dist

            if dists[next_node] <= new_dist:
                continue

            dists[next_node] = new_dist
            heappush(pq, (new_dist, next_node))

    return dists

result = dijkstra(start_node)

for i in range(1, V+1):
    if result[i] == 200001:
        print('INF')
    else:
        print(result[i])