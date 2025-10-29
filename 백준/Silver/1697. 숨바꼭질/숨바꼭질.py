from collections import deque

n, k = map(int, input().split())

MAX = 100000

visited = [-1] * (MAX + 1)

que = deque()
que.append(n)
visited[n] = 0

while que:
    p = que.popleft()

    if p == k:
        print(visited[p])
        break

    next_p1 = p - 1
    if 0 <= next_p1 <= MAX and visited[next_p1] == -1:
        visited[next_p1] = visited[p] + 1
        que.append(next_p1)

    next_p2 = p + 1
    if 0 <= next_p2 <= MAX and visited[next_p2] == -1:
        visited[next_p2] = visited[p] + 1
        que.append(next_p2)

    next_p3 = p * 2
    if 0 <= next_p3 <= MAX and visited[next_p3] == -1:
        visited[next_p3] = visited[p] + 1
        que.append(next_p3)

