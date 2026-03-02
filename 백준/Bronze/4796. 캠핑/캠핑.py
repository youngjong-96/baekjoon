import sys

input = sys.stdin.readline
n = 0

while True:    
    n += 1
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break

    t = V // P
    r = V % P
    if L > r:
        result = L * t + r
    else:
        result = L * t + L
    print(f'Case {n}: {result}')
    