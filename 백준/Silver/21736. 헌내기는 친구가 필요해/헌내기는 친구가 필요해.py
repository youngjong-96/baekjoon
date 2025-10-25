import sys
from collections import deque

"""
O는 빈 공간, X 는 벽, I는 시작점, P는 사람
만날 수 있는 사람 수 출력, 만날 수 있는 사람이 없으면 TT 출력
"""

def find_friend(start):
    cnt = 0
    x, y = start
    que = deque()
    que.append(start)
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1

    while que:
        x, y = que.popleft()
        for dx, dy in delta:
            p, q = x+dx, y+dy
            if 0 <= p < n and 0 <= q < m and arr[p][q] != 'X' and not visited[p][q]:
                if arr[p][q] == 'P':
                    cnt += 1
                visited[p][q] = 1
                que.append((p, q))

    return cnt

n, m = map(int, sys.stdin.readline().strip().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(n)]

x, y = 0, 0
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 시작점 찾기
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'I':
            x, y = i, j

result = find_friend((x, y))

if result == 0:
    print('TT')
else:
    print(result)