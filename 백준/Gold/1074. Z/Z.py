import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

size = 2 ** n
result = 0

while size > 1:
    s = (size * size)//4
    s2 = size // 2
    # 1사분면(우상)
    if s2 > r and s2 <= c:
        result += s
        size //= 2
        c -= s2 
    # 2사분면(좌상)
    elif s2 > r and s2 > c:
        size //= 2
    # 3사분면(좌하)
    elif s2 <= r and s2 > c:
        result += 2 * s
        size //= 2
        r -= s2
    # 4사분면(우하)
    elif s2 <= r and s2 <= c:
        result += 3 * s
        size //= 2
        r -= s2
        c -= s2

print(result)