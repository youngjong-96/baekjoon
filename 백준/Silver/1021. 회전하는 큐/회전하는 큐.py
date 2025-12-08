import sys
from collections import deque



input = sys.stdin.readline

n, m = map(int, input().split())
targets_idx = list(map(int, input().split()))
que = deque(list(range(1, n + 1)))
result = 0

for idx in targets_idx:
    if que.index(idx) <= len(que) // 2:
        while idx != que[0]:
            que.rotate(-1)
            result += 1
        que.popleft()
    else:
        while idx != que[0]:
            que.rotate()
            result += 1
        que.popleft()

print(result)