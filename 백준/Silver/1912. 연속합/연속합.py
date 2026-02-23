import sys

input = sys.stdin.readline

N = int(input().strip())
data = list(map(int, input().split()))

dp = [data[0]] * N

for i in range(1, N):
    dp[i] = max(data[i], dp[i-1] + data[i])

print(max(dp))