import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
numbers = deque(list(range(1, n+1)))
wasted = []

while len(numbers) > 1:
    wasted.append(numbers.popleft())
    numbers.rotate(-1)

result = wasted + list(numbers)
print(*result)