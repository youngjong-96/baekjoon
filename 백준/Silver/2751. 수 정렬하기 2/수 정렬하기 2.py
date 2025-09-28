# 통계학

import sys

n = int(sys.stdin.readline().strip())

fix = 1000000
cnt = [0] * 2000001

for _ in range(n):
    num = int(sys.stdin.readline().strip())
    cnt[num + fix] += 1

for i in range(len(cnt)):
    if cnt[i] > 0:
        for _ in range(cnt[i]):
            print(i - fix)