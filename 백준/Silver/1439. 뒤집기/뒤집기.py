import sys

input = sys.stdin.readline

S = input().strip()

count_0 = 0
count_1 = 0

if S[0] == '0':
    flag = False
    count_0 += 1
else:
    flag = True
    count_1 += 1

for i in S:
    # 이번이 0이고 전에 1이었다면
    if i == '0' and flag:
        count_0 += 1
        flag = False
    # 이번이 1이고 전에 0이었다면
    elif i == '1' and not flag:
        count_1 += 1
        flag = True

if count_1 == 0 or count_1 == 0:
    print(0)
else:
    print(min(count_0, count_1))