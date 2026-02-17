import sys

input = sys.stdin.readline

N, K = map(int, input().split())

data = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    curr_w, curr_v = data[i-1]
    for j in range(1, K + 1):
        if j < curr_w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], curr_v + dp[i-1][j - curr_w])

print(dp[-1][-1])