import sys
from collections import deque
import itertools

def bfs(start_lst):
    que = deque(start_lst)
    visited = [[-1] * n for _ in range(n)]
    # visited 초기화
    for x, y in start_lst:
        visited[x][y] = 0

    while que:
        x, y = que.popleft()
        for dx, dy in delta:
            p, q = x+dx, y+dy
            if 0 <= p < n and 0 <= q < n and visited[p][q] == -1 and arr[p][q] != 1:
                que.append((p, q))
                visited[p][q] = visited[x][y] + 1

    # 안퍼진 공간이 있는지 확인 (벽 제외)
    for i in range(n):
        for j in range(n):
            # 원본 맵에서 벽(1)이 아닌데
            if arr[i][j] != 1:
                # 방문하지 못했다면 (-1)
                if visited[i][j] == -1:
                    return -1  # 전파 불가능
    
    return visited

n, m = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
candidates = []

# 2인 곳 위치 저장
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            candidates.append((i, j))

# c = 후보군들 중 m 곳에 바이러스를 놓는 조합
c = itertools.combinations(candidates, m)
c_lst = list(c)

# 결과
result = float('inf')
cnt = 0

# 가능한 조합별로
for pos in c_lst:
    # bfs를 실행해서 모두 전파가 가능하면 visited 배열 리턴, 불가능하면 -1 리턴
    visited = bfs(pos)
    # 리턴이 -1 이면 cnt + 1
    if visited == -1:
        cnt += 1
    # 리턴이 visited 배열이면(모두 전파가 가능하면)
    else:
        # 전파 시간 계산
        time = 0
        # visited 배열에서 가장 큰 값 찾기(걸린 시간)
        for row in visited:
            if time < max(row):
                time = max(row)
        # 걸린 시간 중 최소값이 최종 결과
        if result > time:
            result = time

if cnt == len(c_lst):
    result = -1

print(result)