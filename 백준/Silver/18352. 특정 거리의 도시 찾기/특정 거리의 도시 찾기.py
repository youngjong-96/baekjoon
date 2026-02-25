import sys
from collections import deque


input = sys.stdin.readline

# 노드수, 간선수, 거리, 출발번호
N, M, K, X = map(int, input().split())
lines = [[] for _ in range(N + 1)]

# 간선 입력받기 (1,000,000)
for _ in range(M):
    s, e = map(int, input().split())
    lines[s].append(e)

que = deque()
visited = [-1] * (N + 1)
que.append(X)
visited[X] = 0

while que:
    q = que.popleft()

    for next_node in lines[q]:
        if visited[next_node] != -1:
            continue

        visited[next_node] = visited[q] + 1
        que.append(next_node)

result = []
for i in range(N+1):
    if visited[i] == K:
        result.append(i)

if result:
    for i in result:
        print(i)
else:
    print(-1)