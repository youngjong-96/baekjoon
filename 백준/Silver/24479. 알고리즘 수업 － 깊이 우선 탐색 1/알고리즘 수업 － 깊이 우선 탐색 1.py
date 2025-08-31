# https://www.acmicpc.net/problem/24479
# DFS1
"""
그래프를 DFS로 탐색하고
각 노드를 순서대로 몇 번째에 방문했는지 출력하는 프로그램을 만드시오
"""
import sys

n, m, r = map(int, sys.stdin.readline().strip().split())

graph = [[] for _ in range(n+1)]

# 그래프 받기
for i in range(m):
    u, v = map(int, sys.stdin.readline().strip().split())

    graph[u].append(v)
    graph[v].append(u)

# 오름차순 탐색을 위해 정렬
for i in range(len(graph)):
    if graph[i]:
        graph[i].sort(reverse=True)

# DFS
visited = [0] * (n+1)
stack = [r]
cnt = 0


while stack:
    t = stack.pop()
    if visited[t] > 0:
        continue

    cnt += 1
    visited[t] = cnt

    for node in graph[t]:
        if not visited[node]:
            stack.append(node)


for i in range(1, n+1):
    print(visited[i])