# 섬의 개수

"""
1 = 땅, 0 = 바다
가로, 세로, 대각선으로 연결되어 있으면 하나의 섬이다
"""

import sys
from collections import deque



def count_island(start):
    global result
    result += 1
    que = deque()
    que.append(start)
    sx, sy = start
    visited[sx][sy] = result

    while que:
        x, y = que.popleft()
        for dx, dy in delta:
            p, q = x+dx, y+dy
            if 0 <= p < n and 0 <= q < m and arr[p][q] == 1 and not visited[p][q]:
                visited[p][q] = result
                que.append((p, q))


while True:
    m, n = map(int, sys.stdin.readline().strip().split())
    if (n, m) == (0, 0):
        break
    arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, 1], [1, 1], [1, -1], [-1, -1]]
    visited = [[0] * m for _ in range(n)]
    result = 0

    start_points = []

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                start_points.append((i, j))

    for point in start_points:
        x, y = point
        if visited[x][y]:
            continue
        count_island(point)

    # for row in visited:
    #     print(*row)
    print(result)