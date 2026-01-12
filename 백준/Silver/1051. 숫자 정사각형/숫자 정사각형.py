import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]

std = n if n < m else m
result = 1

flag = False
for k in range(std-1, 0, -1):
    if flag:
        break
    for i in range(n-k):
        if flag:
            break
        for j in range(m-k):
            if flag:
                break
            if arr[i][j] == arr[i][j+k] == arr[i+k][j] == arr[i+k][j+k]:
                result = (k+1)*(k+1)
                flag = True
                break
print(result)