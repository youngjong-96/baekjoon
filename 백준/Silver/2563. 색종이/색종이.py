white = [[0] * 100 for _ in range(100)]

n = int(input())


for _ in range(n):
    p, q = map(int, input().split())
    for i in range(p, 10+p):
        for j in range(q, 10+q):
            if 0 <= i < 100 and 0 <= j < 100:
                white[i][j] = 1

count = 0

for i in range(100):
    for j in range(100):
        if white[i][j] == 1:
            count += 1

print(count)