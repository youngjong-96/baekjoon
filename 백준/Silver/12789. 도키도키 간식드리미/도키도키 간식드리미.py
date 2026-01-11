import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
numbers = deque(list(map(int, input().split())))

order = 1
result = 'Nice'

stack = []

while numbers:
    if numbers[0] == order:
        order += 1
        numbers.popleft()
        continue
    else:
        if stack:
            if stack[-1] == order:
                order += 1
                stack.pop()
            else:
                stack.append(numbers.popleft())
        else:
            stack.append(numbers.popleft())

while stack:
    if stack[-1] == order:
        order += 1
        stack.pop()
    else:
        if numbers and numbers[0] == order:
            order += 1
            numbers.popleft()
        else:
            result = 'Sad'
            break

print(result)