# 토마토
# 1 = 토마토, 0 = 안 익은 토마토, -1 = 빈 곳
import sys
from collections import deque

def simulate(tomatoes):
    que = deque()
    for tomato in tomatoes:
        que.append(tomato)

    while que:
        x, y = que.popleft()
        for dx, dy in delta:
            p, q = x+dx, y+dy
            if 0 <= p < n and 0 <= q < m and not visited[p][q] and arr[p][q] == 0:
                visited[p][q] = visited[x][y] + 1
                que.append((p, q))
                arr[p][q] = 1


m, n = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]

tomatoes = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            tomatoes.append((i, j))

visited = [[0] * m for _ in range(n)]

simulate(tomatoes)

result = 0
for row in visited:
    r = max(row)
    result = max(result, r)

for row in arr:
    if 0 in row:
        result = -1

print(result)