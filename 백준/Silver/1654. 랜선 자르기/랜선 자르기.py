# 랜선 자르기

import sys
# k=가지고 있는 랜선 수, n=필요한 랜선 수
k, n = map(int, sys.stdin.readline().strip().split())

lines = []

for _ in range(k):
    line = int(sys.stdin.readline().strip())
    lines.append(line)

left = 1
right = max(lines)
result = 0

while left <= right:
    cnt = 0
    std = (left + right) // 2

    for line in lines:
        cnt += line // std

    if cnt >= n:
        result = std
        left = std + 1
    else:
        right = std - 1

print(result)
