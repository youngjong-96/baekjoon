import sys
from itertools import combinations

input = sys.stdin.readline

# 0: 빈칸, 1: 집, 2: 치킨집
# 도시의 치킨 거리는 모든 집에서 가장 가까운 치킨집까지의 거리의 합
# 최대 M개 치킨집을 골랐을 때, 도시의 치킨 거리의 최솟값을 출력
# N: 도시크기, M: 최대 치킨집 수
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

# 두 점 사이의 거리
def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

homes = []
stores = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            homes.append((i, j))
        elif city[i][j] == 2:
            stores.append((i, j))

# [((0, 1),), ((1, 1),), ((2, 1),), ((3, 1),), ((4, 1),)]
stores_case = list(combinations(stores, M))
result = float('inf')

for j in range(len(stores_case)):
    chicken_dist = [N * N] * len(homes)
    for k in range(M):
        for i in range(len(homes)):
            chicken_dist[i] = min(chicken_dist[i], distance(homes[i], stores_case[j][k]))
    result = min(result, sum(chicken_dist))

print(result)