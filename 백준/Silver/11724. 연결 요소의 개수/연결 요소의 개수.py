# 연결 요소의 개수
# https://www.acmicpc.net/problem/11724

import sys
from collections import deque



# 연결 요소 탐색 함수
def bfs(start):
    que = deque()
    que.append(start)
    visited[start] = 1

    while que:
        t = que.popleft()

        for node in graph[t]:
            if not visited[node]:
                que.append(node)
                visited[node] = 1

# n = 노드 수, m = 간선 수
n, m = map(int, sys.stdin.readline().strip().split())

# [[], [2, 5], [1, 5, 4, 3], [4, 2], [3, 6, 5, 2], [2, 1, 4], [4]]
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 1  # 연결요소 개수

# 그래프 입력 받기
for i in range(m):
    s, e = map(int, sys.stdin.readline().strip().split())
    graph[s].append(e)
    graph[e].append(s)

# 일단 1번 연결된 요소부터 확인해서 visited 에 표시
bfs(1)

# 0번 제외하고 연결 안된 노드가 있으면 찾아서 탐색
while 0 in visited[1:]:
    for i in range(1, n+1):
        if visited[i] == 0:
            bfs(i)
            cnt += 1

print(cnt)