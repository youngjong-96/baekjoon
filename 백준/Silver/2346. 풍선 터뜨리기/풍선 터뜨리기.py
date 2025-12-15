import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
data = deque(list(map(int, input().split())))
numbers = deque([])

# numbers = deque([(1, 3), (2, 2), (3, 1), (4, -3), (5, -1)])
for idx, number in enumerate(data):
    numbers.append((idx + 1, number))

while numbers:
    ballon = numbers.popleft()
    idx, number = ballon
    print(idx, end=" ")
    if number > 0:
        number -= 1
        numbers.rotate(-number)
    else:
        numbers.rotate(-number)
