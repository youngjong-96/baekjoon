import sys

input = sys.stdin.readline

n = int(input())
arr = [input().strip() for _ in range(n)]
delta = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
result = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == '.':
            total = 0
            for dx, dy in delta:
                x, y = i+dx, j+dy
                if 0 <= x < n and 0 <= y < n and arr[x][y] != '.':
                    total += int(arr[x][y])
            if total >= 10:
                result[i][j] = 'M'
            else:
                result[i][j] = total
        else:
            result[i][j] = '*'

for row in result:
    print("".join(map(str, row)))