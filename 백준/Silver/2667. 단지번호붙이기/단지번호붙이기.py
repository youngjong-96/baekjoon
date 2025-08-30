# 단지 번호 붙이기

"""
지도에 인접한 집들은 같은 단지로 묶고
총 단지수와 단지별 집 수들을 오름차순으로 출력하기
"""

import sys
from collections import deque

# 지도 크기
n = int(sys.stdin.readline())
# 지도
arr = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]

# 단지
dong = 0
# 단지별 집 수 받을 배열
house = []

visited = [[0] * n for _ in range(n)]

# 지도를 순서대로 순회하면서
for i in range(n):
    for j in range(n):
        # 집이 있는 곳을 만나면
        if arr[i][j] == '1':
            # 새로운 동으로 표시하기 위해 동 += 1
            dong += 1

            # 해당 위치를 enque 하고 visited 배열에 단지로 표시한다
            que = deque()
            que.append((i,j))
            visited[i][j] = dong

            # DFS 수행하면서 인접한 단지를 탐색한다
            cnt = 1
            while que:
                x, y = que.popleft()
                #                하     상     우     좌
                for dx, dy in [[1,0],[-1,0],[0,1],[0,-1]]:
                    p, q = x+dx, y+dy
                    if 0 <= p < n and 0 <= q < n and arr[p][q] == '1' and not visited[p][q]:
                        que.append((p,q))
                        visited[p][q] = dong
                        cnt += 1
                        # 다시 탐색하지 않도록 원본 배열에서 0으로 수정
                        arr[p][q] = 0
            # 같은 단지의 집 수를 저장한다
            house.append(cnt)

house.sort()
print(dong)
for i in range(len(house)):
    print(house[i])