import sys

input = sys.stdin.readline

N = int(input().strip())
data = [int(input().strip()) for _ in range(N)]

data.sort()

result = -1
numbers = data[:3]

if numbers[2] < numbers[0] + numbers[1]:
    result = sum(numbers[:3])

if N > 3:
    for i in range(3, N):
        numbers.pop(0)
        numbers.append(data[i])
        if numbers[2] < numbers[0] + numbers[1]:
            result = max(result, sum(numbers[:3]))

print(result)