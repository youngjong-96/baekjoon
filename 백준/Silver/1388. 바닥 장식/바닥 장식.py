import sys
from collections import deque


def bfs(start):
    x, y = start
    que = deque()
    visited[x][y] = 1
    que.append((x, y))

    while que:
        x, y = que.popleft()
        if tiles[x][y] == '-':
            delta = delta1
        else:
            delta = delta2
        for dx, dy in delta:
            p, q = x+dx, y+dy
            if 0 <= p < n and 0 <= q < m and not visited[p][q] and tiles[x][y] == tiles[p][q]:
                visited[p][q] = 1
                que.append((p, q))


n, m = map(int, sys.stdin.readline().strip().split())
# ['----', '----', '----', '----']
tiles = [sys.stdin.readline().strip() for _ in range(n)]
delta1 = [(0, -1), (0, 1)]  # '-'
delta2 = [(-1, 0), (1, 0)]  # 'ㅣ'
visited = [[0] * m for _ in range(n)]

cnt = 0
# 50 x 50
for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue
        else:
            cnt += 1
            bfs((i, j))

print(cnt)