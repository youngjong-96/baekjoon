import sys

input = sys.stdin.readline

def time(t, m):
    if 0 <= t <= 23 and 0 <= m <= 59:
        return True
    return False

def month(m, d):
    if m in [1, 3, 5, 7, 8, 10, 12] and 1 <= d <= 31:
        return True
    elif m in [4, 6, 9, 11] and 1 <= d <= 30:
        return True
    elif m == 2 and 1 <= d <= 29:
        return True
    else:
        return False

T = int(input().strip())

for _ in range(T):
    x, y = map(int, input().split())
    
    if time(x, y):
        print('Yes', end=" ")
    else:
        print('No', end=" ")
    
    if month(x, y):
        print('Yes')
    else:
        print('No')