import sys

n = int(sys.stdin.readline().strip())

data = []

for _ in range(n):
    xi, yi = map(int, sys.stdin.readline().strip().split())
    data.append((xi, yi))

data.sort(key=lambda x: (x[0], x[1]))

for x, y in data:
    print(x, y)