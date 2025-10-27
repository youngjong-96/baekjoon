import sys

numbers = [0] * 101
numbers[0] = 1
numbers[1] = 1
numbers[2] = 1
numbers[3] = 2
numbers[4] = 2
numbers[5] = 3
numbers[6] = 4
numbers[7] = 5
for i in range(8, 101):
    numbers[i] = numbers[i-5] + numbers[i-1]

T = int(sys.stdin.readline().strip())
for _ in range(T):
    n = int(sys.stdin.readline().strip())
    print(numbers[n-1])