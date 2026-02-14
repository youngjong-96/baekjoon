import sys
from collections import deque

#sys.stdin = open('sample_input.txt', 'r')
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    A, B = map(int, input().split())
    visited = [0] * 10000

    q = deque([(A, "")])
    visited[A] = 1

    while q:
        n, path = q.popleft()

        if n == B:
            print(path)
            break

        dn = (n * 2) % 10000
        if not visited[dn]:
            visited[dn] = 1
            q.append((dn, path + "D"))

        sn = (n - 1) % 10000
        if not visited[sn]:
            visited[sn] = 1
            q.append((sn, path + "S"))

        ln = (n % 1000) * 10 + (n // 1000)
        if not visited[ln]:
            visited[ln] = 1
            q.append((ln, path + "L"))

        rn = (n % 10) * 1000 + (n // 10)
        if not visited[rn]:
            visited[rn] = 1
            q.append((rn, path + "R"))