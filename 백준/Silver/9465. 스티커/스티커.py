import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    n = int(sys.stdin.readline().strip())
    # 2xn의 2차원 배열 (1 <= n <= 100,000)
    stickers = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]

    # n=1 인 경우 처리
    if n == 1:
        print(max(stickers[0][0], stickers[1][0]))
    else:
        # 초기값 설정 - 두 번째 열까지
        dp[0][0] = stickers[0][0]
        dp[1][0] = stickers[1][0]
        dp[0][1] = stickers[0][1] + stickers[1][0]
        dp[1][1] = stickers[1][1] + stickers[0][0]

        for j in range(2, n):
            for i in range(2):
                if i == 0:
                    dp[i][j] = max(dp[0][j-2] + stickers[1][j-1] + stickers[0][j], dp[1][j-2] + stickers[0][j], dp[1][j-1] + stickers[0][j])
                else:
                    dp[i][j] = max(dp[1][j-2] + stickers[0][j-1] + stickers[1][j], dp[0][j-2] + stickers[1][j], dp[0][j-1] + stickers[1][j])

        print(max(dp[0][n-1], dp[1][n-1]))