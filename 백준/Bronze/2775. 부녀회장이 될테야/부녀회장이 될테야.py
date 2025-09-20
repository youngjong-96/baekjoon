
# 부녀회장이 될테야
T = int(input())
for t in range(T):
    # 층, 호수
    k = int(input())
    n = int(input())
    apt = [[0] * (n + 1) for _ in range(k + 1)]

    for i in range(n + 1):
        apt[0][i] = i

    for i in range(1, k + 1):
        for j in range(1, n + 1):
            apt[i][j] = apt[i][j-1] + apt[i-1][j]

    print(apt[k][n])