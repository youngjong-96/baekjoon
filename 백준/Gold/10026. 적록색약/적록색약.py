import sys
from collections import deque

def normal(start):
    x, y = start
    que = deque()
    que.append((x, y))
    visited[x][y] = 1

    while que:
        x, y = que.popleft()
        for dx, dy in delta:
            p, q = x+dx, y+dy
            if 0 <= p < n and 0 <= q < n and arr[p][q] == arr[x][y] and not visited[p][q]:
                que.append((p, q))
                visited[p][q] = visited[x][y]

def color(start):
    x, y = start
    que = deque()
    que.append((x, y))
    visited_c[x][y] = 1

    while que:
        x, y = que.popleft()
        for dx, dy in delta:
            p, q = x+dx, y+dy
            if 0 <= p < n and 0 <= q < n and not visited_c[p][q]:
                if arr[x][y] == 'B' and arr[p][q] == 'B':
                    que.append((p, q))
                    visited_c[p][q] = visited_c[x][y]
                if arr[x][y] in ('R', 'G') and arr[p][q] in ('R', 'G'):
                    que.append((p, q))
                    visited_c[p][q] = visited_c[x][y]

# 크기
n = int(sys.stdin.readline().strip())
# 배열
arr = [list(sys.stdin.readline().strip()) for _ in range(n)]

# visited 배열, 일반, 색맹
visited = [[0] * n for _ in range(n)]
visited_c = [[0] * n for _ in range(n)]

# delta = 상, 하, 좌, 우
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 결과
result = 0
result_c = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            result += 1
            normal((i, j))

for i in range(n):
    for j in range(n):
        if visited_c[i][j] == 0:
            result_c += 1
            color((i, j))

print(result, result_c)