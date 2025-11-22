import sys

n = int(sys.stdin.readline().strip())

Q1 = []
Q2 = []
Q3 = []
Q4 = []
axis = []
dotes = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    dotes.append((x, y))

for dot in dotes:
    x, y = dot
    if x > 0 and y > 0:
        Q1.append(dot)
    elif x > 0 and y < 0:
        Q4.append(dot)
    elif x < 0 and y > 0:
        Q2.append(dot)
    elif x < 0 and y < 0:
        Q3.append(dot)
    else:
        axis.append(dot)

print(f'Q1: {len(Q1)}')
print(f'Q2: {len(Q2)}')
print(f'Q3: {len(Q3)}')
print(f'Q4: {len(Q4)}')
print(f'AXIS: {len(axis)}')