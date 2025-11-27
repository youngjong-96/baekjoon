import sys

input = sys.stdin.readline

H, W = map(int, input().split())
N = int(input())

# [(1, 2), (2, 1)]
stickers = []
for _ in range(N):
    R, C = map(int, input().split())
    stickers.append((R, C))

result = 0
for i in range(N-1):
    for j in range(i+1, N):
        s1 = stickers[i]
        s2 = stickers[j]
        if s1[0] + s2[0] <= W and s1[1] <= H and s2[1] <= H:
            result = max(result, s1[0] * s1[1] + s2[0] * s2[1])
        if s1[0] + s2[1] <= W and s1[1] <= H and s2[0] <= H:
            result = max(result, s1[0] * s1[1] + s2[0] * s2[1])
        if s1[1] + s2[0] <= W and s1[0] <= H and s2[1] <= H:
            result = max(result, s1[0] * s1[1] + s2[0] * s2[1])
        if s1[1] + s2[1] <= W and s1[0] <= H and s2[0] <= H:
            result = max(result, s1[0] * s1[1] + s2[0] * s2[1])

        if s1[0] + s2[0] <= H and s1[1] <= W and s2[1] <= W:
            result = max(result, s1[0] * s1[1] + s2[0] * s2[1])
        if s1[0] + s2[1] <= H and s1[1] <= W and s2[0] <= W:
            result = max(result, s1[0] * s1[1] + s2[0] * s2[1])
        if s1[1] + s2[0] <= H and s1[0] <= W and s2[1] <= W:
            result = max(result, s1[0] * s1[1] + s2[0] * s2[1])
        if s1[1] + s2[1] <= H and s1[0] <= W and s2[0] <= W:
            result = max(result, s1[0] * s1[1] + s2[0] * s2[1])

print(result)