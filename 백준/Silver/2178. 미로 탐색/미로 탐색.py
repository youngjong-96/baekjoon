# 미로

"""
n x m 크기 미로
1 = 이동 가능, 0 = 이동 불가
(1,1)에서 출발, (n,m)의 위치로 이동할 때 지나야 하는 최소의 칸 수 구하기
칸을 셀 때는 시작위치와 도착위치도 포함
"""
import sys
from collections import deque

# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다.
n, m = map(int, sys.stdin.readline().strip().split())

# 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.
arr = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]


visited = [[0] * m for _ in range(n)]
que = deque()
que.append((0,0))
visited[0][0] = 1

while que:
    a, b = que.popleft()

    for di, dj in [[-1,0], [1,0], [0,-1],[0,1]]:
        p, q = a+di, b+dj
        if 0 <= p < n and 0 <= q < m and arr[p][q] == '1' and not visited[p][q]:
            que.append((p,q))
            visited[p][q] = visited[a][b] + 1


print(visited[n-1][m-1])