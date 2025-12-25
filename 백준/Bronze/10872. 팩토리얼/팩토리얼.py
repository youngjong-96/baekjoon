import sys

input = sys.stdin.readline

n = int(input())
result = 1
if n == 0 or n == 1:
    print(result)
else:
    for i in range(2, n+1):
        result *= i
    print(result)