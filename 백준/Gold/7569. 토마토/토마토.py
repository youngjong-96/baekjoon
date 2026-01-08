import sys
input = sys.stdin.readline
from collections import deque

# m=열, n=행, h=층
m, n, h = map(int, input().split())

# [[[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 1], [0, 0]]]
buckets = [list(list(map(int, input().split())) for _ in range(n)) for _ in range(h)]

# 상, 하, 좌, 우, 앞, 뒤
delta = [(0, -1, 0), 
         (0, 1, 0), 
         (0, 0, -1), 
         (0, 0, 1), 
         (-1, 0, 0), 
         (1, 0, 0)]

# 초기 토마토 위치 찾기
tomatoes = []
for i in range(h):
    for j in range(n):
        for k in range(m):
            if buckets[i][j][k] == 1:
                tomatoes.append((i, j, k))

def bfs(start):
    que = deque(start)
    visited = list(list([0] * m for _ in range(n)) for _ in range(h))
    for x, y, z in start:
        visited[x][y][z] = 1
    
    while que:
        tomato = que.popleft()
        x, y, z = tomato
    
        for dx, dy, dz in delta:
            # 범위조건
            p, q, r = x+dx, y+dy, z+dz
            if p < 0 or p >= h:
                continue
            if q < 0 or q >= n:
                continue
            if r < 0 or r >= m:
                continue
            # 방문한적이 없고, 익지 않은 토마토가 있으면
            if not visited[p][q][r] and buckets[p][q][r] == 0:
                visited[p][q][r] = visited[x][y][z] + 1
                que.append((p, q, r))
    return visited

result = bfs(tomatoes)

day = 0
flag = False

for i in range(h):
    if flag:
        break
    for j in range(n):
        if flag:
            break
        for k in range(m):
            # 익지 못하는 토마토가 있는 경우
            if buckets[i][j][k] == 0 and result[i][j][k] == 0:
                day = -1
                flag = True
                break
            # 걸리는 날 계산
            else:
                day = max(day, result[i][j][k])

if day != -1:
    day -= 1
print(day)