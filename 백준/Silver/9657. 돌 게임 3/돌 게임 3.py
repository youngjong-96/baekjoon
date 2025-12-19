import sys


input = sys.stdin.readline

n = int(input())

dp = [""] * 1005

dp[1] = 'win'
dp[2] = 'loss'
dp[3] = 'win'
dp[4] = 'win'

for i in range(5, n+1):
    if dp[i-1] == 'loss' or dp[i-3] == 'loss' or dp[i-4] == 'loss':
        dp[i] = 'win'
    else:
        dp[i] = 'loss'

if dp[n] == 'win':
    print("SK")
else:
    print("CY")