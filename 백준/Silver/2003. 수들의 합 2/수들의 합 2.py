import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
cnt = 0

s, e = 0, 1
while s <= n and e <= n:
    if sum(numbers[s:e]) == m:
        cnt += 1
        s += 1
        e = s + 1
    elif sum(numbers[s:e]) < m and s <= e:
        e += 1
    elif sum(numbers[s:e]) > m and s <= e:
        s += 1
        e = s + 1
    else:
        s += 1
        e = s + 1
print(cnt)