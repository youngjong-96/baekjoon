import sys

input = sys.stdin.readline

N = int(input().strip())
T = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(len(T[i])):
        if j == 0: # 왼쪽 끝
            T[i][j] += T[i-1][j]
        elif j == i: # 오른쪽 끝
            T[i][j] += T[i-1][j-1]
        else:
            T[i][j] += max(T[i-1][j-1], T[i-1][j])

print(max(T[N - 1]))