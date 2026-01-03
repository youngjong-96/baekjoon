import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

graph = [[] for _ in range(n+1)]
for i in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

check = [0] * (n+1)
que = deque([1])
check[1] = 1

while que:
    p = que.popleft()

    if check[p] == 3:
        continue

    for next_p in graph[p]:
        if check[next_p] == 0:
            check[next_p] = check[p] + 1
            que.append(next_p)

result = 0
for i in range(2, n+1):
    if 1 < check[i] <= 3:
        result += 1
print(result)