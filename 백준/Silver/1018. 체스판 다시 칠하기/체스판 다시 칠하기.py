import sys

def check(x, y):
    result1 = 0
    result2 = 0

    for i in range(8):
        for j in range(8):
            if arr[i+x][j+y] != case1[i][j]:
                result1 += 1

    for i in range(8):
        for j in range(8):
            if arr[i+x][j+y] != case2[i][j]:
                result2 += 1

    return min(result1, result2)

n, m = map(int, sys.stdin.readline().strip().split())
arr = [sys.stdin.readline().strip() for _ in range(n)]

case1 = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
]
case2 = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
]

result = 64

for i in range(n-7):
    for j in range(m-7):
        t = check(i, j)
        result = min(t, result)

print(result)