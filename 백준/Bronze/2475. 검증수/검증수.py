import sys

numbers = list(map(int, sys.stdin.readline().strip().split()))

result = 0

for i in range(len(numbers)):
    result += numbers[i] ** 2

print(result % 10)