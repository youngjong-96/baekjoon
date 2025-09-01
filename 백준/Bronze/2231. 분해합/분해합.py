# 분해합
import sys

def hap(num):
    original = num
    s = 0
    while num >= 10:
        s += num % 10
        num //= 10
    original += s
    original += num

    return original

n = int(sys.stdin.readline().strip())
ans = 0
for i in range(1, n):
    if hap(i) == n:
        ans = i
        break

print(ans)