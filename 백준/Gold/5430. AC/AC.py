import sys
from collections import deque

T = int(sys.stdin.readline().strip())

for t in range(T):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    xi = sys.stdin.readline().strip()

    if n == 0:
        numbers = deque()
    else:
        numbers = deque(xi[1:-1].split(','))

    is_reversed = False
    is_error = False

    for command in p:
        if command == 'R':
            is_reversed = not is_reversed
        else:
            if not numbers:
                is_error = True
                break

            if is_reversed:
                numbers.pop()
            else:
                numbers.popleft()

    if is_error:
        print('error')
    else:
        if is_reversed:
            numbers.reverse()
        print(f"[{','.join(numbers)}]")