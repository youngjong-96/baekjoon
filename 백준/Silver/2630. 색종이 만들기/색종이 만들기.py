# 색종이 만들기

import sys
from collections import deque

def check(paper):
    x, y = paper
    xs, xe = x
    ys, ye = y

    if arr[xs][ys] == 1:
        flag = 1
    else:
        flag = 0

    for i in range(xs, xe):
        for j in range(ys, ye):
            if arr[i][j] != flag:
                return 3

    return flag


n = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

check_list = deque([((0, n), (0, n))])
white = 0
blue = 0

while check_list:
    paper = check_list.popleft()

    result = check(paper)

    if result == 0:
        white += 1
    elif result == 1:
        blue += 1
    else:
        xs, xe = paper[0]
        ys, ye = paper[1]

        mid_x = xs + (xe - xs) // 2
        mid_y = ys + (ye - ys) // 2

        check_list.append(((xs, mid_x), (ys, mid_y)))
        check_list.append(((xs, mid_x), (mid_y, ye)))
        check_list.append(((mid_x, xe), (ys, mid_y)))
        check_list.append(((mid_x, xe), (mid_y, ye)))


print(white)
print(blue)
