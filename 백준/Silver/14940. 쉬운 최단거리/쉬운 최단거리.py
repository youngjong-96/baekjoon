# 쉬운 최단거리

# 모든 지좀에 대해서 목표지점까지의 거리를 구하여라
# 가로 세로로만 움직일 수 있다
# 0 = 갈수 없는 땅, 1 = 갈 수 있는 땅, 2 = 목표
# 원래 갈 수 없는 땅인 0은 0을 출력하고, 도달할 수 없는 곳은 -1을 출력

import sys
from collections import deque


n, m = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]

sx, sy = 0, 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            sx, sy = i, j

que = deque([(sx, sy)])
visited = [[-1] * m for _ in range(n)]
visited[sx][sy] = 0

while que:
    r, c = que.popleft()
    for dx, dy in delta:
        p, q = r+dx, c+dy
        if not (0 <= p < n):
            continue

        if not (0 <= q < m):
            continue

        if visited[p][q] != -1:
            continue

        if arr[p][q] == 0:
            continue

        visited[p][q] = visited[r][c] + 1
        que.append((p, q))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            visited[i][j] = 0

for row in visited:
    print(*row)