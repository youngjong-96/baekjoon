import sys

input = sys.stdin.readline

n, m = map(int, input().split())

def recur():
    if len(path) == m:
        print(*path)
        return
    
    for i in range(1, n+1):
        path.append(i)
        recur()
        path.pop()

visited = []
path = []
recur()