import sys

input = sys.stdin.readline

N, L = map(int, input().split())

for i in range(L, 101):
    x = (N - (i * (i - 1) // 2))
    if (x // i) >= 0 and x % i == 0:
        x = x // i
        for j in range(i):
            print(x+j, end=" ")
        break
else:
    print(-1)