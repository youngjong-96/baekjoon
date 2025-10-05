# n과 m 5
import sys

def recur(pick):
    if pick == m:
        print(*path)
        return

    for i in candidates:
        if i in path:
            continue
        path.append(i)
        recur(pick + 1)
        path.pop()

n, m = map(int, sys.stdin.readline().strip().split())
candidates = list(map(int, sys.stdin.readline().strip().split()))
candidates.sort()

path = []
recur(0)
