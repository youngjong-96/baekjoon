import sys

input = sys.stdin.readline

N = int(input().strip())
numbers = [int(input().strip()) for _ in range(N)]
s_numbers = sorted(numbers)

for i in s_numbers:
    print(i)