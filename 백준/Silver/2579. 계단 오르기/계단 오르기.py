import sys

n = int(sys.stdin.readline().strip())
if n == 0:
    print(0)
    sys.exit()

scores = [0] * n
for i in range(n):
    scores[i] = int(sys.stdin.readline().strip())

dp = [0] * n

dp[0] = scores[0]

if n >= 2:
    dp[1] = scores[0] + scores[1]

if n >= 3:
    dp[2] = max(dp[0] + scores[2], scores[1] + scores[2]) 
    
    for i in range(3, n):
        dp[i] = max(dp[i-3] + scores[i-1] + scores[i], 
                    dp[i-2] + scores[i])


print(dp[n-1])