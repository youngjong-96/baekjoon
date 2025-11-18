import sys

n = int(sys.stdin.readline().strip())

# 자연수 i를 나타내기 위한 최소 제곱수 개수
dp = [4] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    k = 1
    while k * k <= i:
        k_squared = k * k
        dp[i] = min(dp[i], dp[i - k_squared] + 1)
        k += 1

print(dp[n])