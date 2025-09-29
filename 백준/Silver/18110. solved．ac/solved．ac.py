# solved.ac

import sys

n = int(sys.stdin.readline().strip())
numbers = []
for _ in range(n):
    numbers.append(int(sys.stdin.readline().strip()))
numbers.sort()

per = int(n * 0.15 + 0.5)

if n - (per * 2) == 0:
    print(0)
else:
    avg = sum(numbers[per:n - per]) / (n - (per * 2))
    print(int(avg + 0.5))
