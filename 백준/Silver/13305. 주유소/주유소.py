import sys

input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

total_cost = 0
min_price = cost[0]  

for i in range(n - 1):
    # 현재까지 지나온 주유소 중 가장 저렴한 가격을 선택
    if cost[i] < min_price:
        min_price = cost[i]

    # 그 가격으로 다음 도시까지의 거리를 곱해 더함
    total_cost += min_price * dist[i]

print(total_cost)