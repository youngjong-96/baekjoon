import sys

input = sys.stdin.readline

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]

# dp[상태][r][c]: (r, c) 위치에 '상태'로 도착하는 경우의 수
# 상태: 0(가로), 1(세로), 2(대각선)
dp = [[[0] * N for _ in range(N)] for _ in range(3)]

# 초기값 설정 (1행 2열에 가로로 놓여있음)
dp[0][0][1] = 1

for r in range(N):
    for c in range(N):
        # 벽인 경우 패스
        if house[r][c] == 1:
            continue

        # 1. 가로 상태로 오는 경우
        if c + 1 < N and house[r][c+1] == 0:
            dp[0][r][c+1] += (dp[0][r][c] + dp[2][r][c])

        # 2. 세로 상태로 오는 경우
        if r + 1 < N and house[r+1][c] == 0:
            dp[1][r+1][c] += (dp[1][r][c] + dp[2][r][c])

        # 3. 대각선 상태로 오는 경우
        if r + 1 < N and c + 1 < N:
            if house[r+1][c] == 0 and house[r][c+1] == 0 and house[r+1][c+1] == 0:
                dp[2][r+1][c+1] += (dp[0][r][c] + dp[1][r][c] + dp[2][r][c])

# 마지막 칸에 도달하는 모든 상태의 합 출력
print(dp[0][N-1][N-1] + dp[1][N-1][N-1] + dp[2][N-1][N-1])