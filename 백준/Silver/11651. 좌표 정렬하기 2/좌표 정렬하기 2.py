import sys

n = int(sys.stdin.readline().strip())
dots = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    dots.append((x, y))

dots.sort(key=lambda x: (x[1], x[0]))

for dot in dots:
    print(*dot)