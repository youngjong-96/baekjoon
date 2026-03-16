import sys

input = sys.stdin.readline

N = int(input().strip())
data = [0] + [int(input().strip()) for _ in range(N)]

if N == 1:
    print(data[1])
else:
    dp = [0] * (N + 1)
    dp[1] = data[1]
    if N >= 2:
        dp[2] = data[1] + data[2]

    for i in range(3, N + 1):
        dp[i] = max(dp[i-1], dp[i-2] + data[i], dp[i-3] + data[i-1] + data[i])
    
    print(dp[N])