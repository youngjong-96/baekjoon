import sys

input = sys.stdin.readline

n = int(input().strip())
data = list(map(int, input().split()))

result = [0] * n

for i in range(n):
    cnt_t = data[i]  # 나보다 큰 사람
    cnt = 0   # 빈자리

    for j in range(n):
        if not result[j]:
            if cnt == cnt_t:
                result[j] = i + 1
                break
            cnt += 1

print(*result)