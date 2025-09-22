# 덩치

def check(p1, p2):
    w1, h1, num = p1
    w2, h2, num = p2
    if w2 > w1 and h2 > h1:
        return 1
    else:
        return 0

n = int(input())

# 몸무게, 키, 입력 순서
data = []

for i in range(n):
    w, h = map(int,input().split())
    data.append([w, h, i])

data.sort(key=lambda x:(x[0], x[1]))

for i in range(n-1):
    cnt = 0
    for j in range(i + 1, n):
        cnt += check(data[i], data[j])
    data[i].append(cnt + 1)

data[n-1].append(1)

data.sort(key=lambda x:x[2])

for i in range(n):
    print(data[i][3], end=" ")