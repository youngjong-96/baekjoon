import sys

# 입력을 빠르게 받기 위해 readline 사용
input = sys.stdin.readline

# n: 표의 크기, m: 합을 구해야 하는 횟수
n, m = map(int, input().split())

# 원본 2차원 배열 입력 받기
arr = [list(map(int, input().split())) for _ in range(n)]

# 2차원 누적 합을 저장할 DP 테이블 (크기를 n+1 x n+1로 만들어 패딩)
dp = [[0] * (n + 1) for _ in range(n + 1)]

# DP 테이블 채우기
# dp[i][j]는 (1,1)부터 (i,j)까지의 사각형 구간 합을 의미
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 점화식 적용
        dp[i][j] = arr[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

# m번의 쿼리에 대해 구간 합 계산 및 출력
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    # 2차원 구간 합 공식 적용
    result = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]
    print(result)