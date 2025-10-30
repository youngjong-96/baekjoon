import sys

# n, m = 가로, 세로, b = 블럭개수
n, m, b = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

height_lst = [0] * 257

height_counts = [0] * 257
for i in range(n):
    for j in range(m):
        height_counts[arr[i][j]] += 1

for k in range(257):
    b_cnt = b
    time_taken = 0

    for h in range(257):
        count = height_counts[h]
        if count == 0: continue

        if h >= k:
            time_taken += (h - k) * 2 * count
            b_cnt += (h - k) * count
        else:
            time_taken += (k - h) * 1 * count
            b_cnt -= (k - h) * count

    if b_cnt < 0:
        height_lst[k] = float('inf')
    else:
        height_lst[k] = time_taken

t = float('inf')
h = 0
for i in range(len(height_lst)):
    if height_lst[i] <= t:
        t = height_lst[i]
        h = i

print(t, h)