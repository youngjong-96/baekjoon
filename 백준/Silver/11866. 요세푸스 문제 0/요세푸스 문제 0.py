n, k = map(int, input().split())

numbers = [i for i in range(1, n + 1)]
visited = [0] * n
result = []

p = -1

cnt = 0
while 0 in visited:
    p = (p + 1) % n
    if visited[p] == 0:
        cnt += 1
        if cnt == k:
            result.append(numbers[p])
            visited[p] = 1
            cnt = 0

print('<', end='')
print(", ".join(map(str, result)), end="")
print('>')