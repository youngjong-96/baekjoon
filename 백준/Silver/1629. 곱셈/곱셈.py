import sys
sys.setrecursionlimit(10**4)

def recur(A, B, C):
    if B == 1:
        return A % C

    temp = recur(A, B//2, C)

    if B % 2 == 0:
        return (temp * temp) % C
    else:
        return (temp * temp * A) % C

a, b, c = map(int, input().split())

if b == 0:
    print(1 % c)
else:
    result = recur(a, b, c)
    print(result)