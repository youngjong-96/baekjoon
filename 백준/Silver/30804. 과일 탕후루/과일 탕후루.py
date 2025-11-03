import sys

input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))

f_lst = {}

left = 0
result = 0

for r in range(n):
    current_fruit = s[r]

    f_lst[current_fruit] = f_lst.get(current_fruit, 0) + 1

    while len(f_lst) > 2:
        left_fruit = s[left]
        f_lst[left_fruit] -= 1

        # 만약 해당 과일의 개수가 0이 되면 딕셔너리에서 키를 삭제
        if f_lst[left_fruit] == 0:
            del f_lst[left_fruit]

        left += 1

    result = max(result, r - left + 1)

print(result)