#  유기농 배추

import sys
from collections import deque

T = int(sys.stdin.readline().strip())
for t in range(T):
    n, m, k = map(int, sys.stdin.readline().strip().split())

    arr = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().strip().split())
        arr[x][y] = 1


    visited = [[0] * m for _ in range(n)]
    que = deque()
    cnt = 0

    # 배추밭을 확인하면서
    for i in range(n):
        for j in range(m):
            # 배추를 찾으면 que에 넣는다
            if arr[i][j] == 1:
                que.append((i, j))
                # 처음 보는 배추는 cnt를 올린다
                if not visited[i][j]:
                    cnt += 1
                # 배추밭 근처에 있는 배추들을 모두 같은 cnt로 표시한다
                while que:
                    a, b = que.popleft()
                    visited[a][b] = cnt
                    # 델타 (상, 하, 우, 좌)
                    for di, dj in [[1,0], [-1,0], [0,1], [0,-1]]:
                        p, q = a+di, b+dj
                        # 배추밭 범위이고, 배추가 있고, 방문한 적이 없으면
                        if 0 <= p < n and 0 <= q < m and arr[p][q] == 1 and not visited[p][q]:
                            que.append((p,q))
                            visited[p][q] = cnt

    print(cnt)