# DFS와 BFS

"""
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다.
정점 번호는 1번부터 N번까지이다.
"""
import sys
from collections import deque

def dfs(start):
    visited = [0] * (n+1)
    stack = deque()
    stack.append(start)
    basket = []

    while stack:
        t = stack.pop()
        if not visited[t]:
            visited[t] = 1
            basket.append(t)
            for node in reversed(graph[t]):
                if not visited[node]:
                    stack.append(node)

    return " ".join(map(str, basket))


def bfs(start):
    visited = [0] * (n + 1)
    que = deque()
    que.append(start)
    visited[start] = 1
    basket2 = [start]

    while que:
        t = que.popleft()
        for node in graph[t]:
            if not visited[node]:
                visited[node] = 1
                que.append(node)
                basket2.append(node)

    return " ".join(map(str, basket2))

# 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
n, m, v = map(int, sys.stdin.readline().strip().split())

# 그래프 만들기 - 인접 리스트
graph = [[] for _ in range(n+1)]

# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
# 입력으로 주어지는 간선은 양방향이다.
for i in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

print(dfs(v))
print(bfs(v))