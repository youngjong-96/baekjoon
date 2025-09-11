# 동전 0

import sys


n, k = map(int, sys.stdin.readline().strip().split())

coins = []
for i in range(n):
    coins.append(int(sys.stdin.readline().strip()))

coins.reverse()
result = 0

while k > 0:
    for i in range(n): # n 개 코인 확인
        if k >= coins[i]:  # 거슬러 줄 수 있는 코인이면
            result += k // coins[i]
            k %= coins[i]

print(result)