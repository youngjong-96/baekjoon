import sys

input = sys.stdin.readline

N = int(input().strip())
T, B = 1, 5000

for _ in range(N):
    t, b = map(int, input().strip().split())
    T = max(t, T)
    B = min(b, B)

num = T * B

print(num % 7 + 1)