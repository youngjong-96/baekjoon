# 소수 찾기

import sys

n = int(sys.stdin.readline().strip())

numbers = list(map(int, sys.stdin.readline().strip().split()))

cnt = 0

for num in numbers:
    if num == 1:
        continue
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        cnt += 1

print(cnt)