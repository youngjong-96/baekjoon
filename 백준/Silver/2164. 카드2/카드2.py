# 카드 2

import sys
from collections import deque


def turn():
    que.popleft()
    t = que.popleft()
    que.append(t)

que = deque()

n = int(sys.stdin.readline())

for i in range(1, n+1):
    que.append(i)

while len(que) > 1:
    turn()

print(que.popleft())
