import sys


input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

max_friend_count = -1
result_student = 0


for i in range(n):
    count = 0
    for j in range(n):
        if i == j:
            continue

        for k in range(5):
            if data[i][k] == data[j][k]:
                count += 1
                break

    if count > max_friend_count:
        max_friend_count = count
        result_student = i + 1

print(result_student)