import sys

input = sys.stdin.readline

N, K = map(int, input().split())

data = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0] * (K + 1)

for i in range(N):
    curr_w, curr_v = data[i]
    for j in range(K, curr_w - 1, -1):
        dp[j] = max(dp[j], dp[j - curr_w] + curr_v)

print(dp[K])