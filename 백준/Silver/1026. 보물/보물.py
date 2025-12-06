import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = 0

while A:
    a = min(A)
    b = max(B)
    result += a * b
    A.remove(a)
    B.remove(b)

print(result)