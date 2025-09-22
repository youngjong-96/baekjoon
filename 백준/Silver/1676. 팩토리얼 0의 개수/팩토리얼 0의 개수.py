n = int(input())

arr = [0] * (n + 1)

arr[0] = 1
if n > 0:
    arr[1] = 1

for i in range(2, n + 1):
    arr[i] = i * arr[i - 1]

num = str(arr[n])

cnt = 0

for s in num[len(num)::-1]:
    if int(s) == 0:
        cnt += 1
    else:
        break

print(cnt)