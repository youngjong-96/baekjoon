import sys

input = sys.stdin.readline

arr = [input().split() for _ in range(5)]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
results = set()

def dfs(x, y, string):
    # 6자리가 되면 종료
    if len(string) == 6:
        results.add(string)
        return

    for dx, dy in delta:
        p, q = x+dx, y+dy
        if p < 0 or p >= 5:
            continue
        if q < 0 or q >= 5:
            continue
        dfs(p, q, string + arr[p][q])

for i in range(5):
    for j in range(5):
        dfs(i, j, arr[i][j])

print(len(results))