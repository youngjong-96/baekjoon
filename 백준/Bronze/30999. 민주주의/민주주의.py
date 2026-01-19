import sys

input = sys.stdin.readline

n, m = map(int, input().split())

data = [list(input().strip()) for _ in range(n)]

result = 0
for i in range(n):
    cnt = 0
    for j in range(m):
        if data[i][j] == 'O':
            cnt += 1
    if cnt > m//2:
        result += 1
print(result)