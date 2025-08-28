# 팰린드롬수

import sys

while True:
    number = list(sys.stdin.readline().strip())
    if number == ['0']:
        break

    n = len(number) // 2

    for i in range(n):
        if number[i] != number[-(i + 1)]:
            print('no')
            break
    else:
        print('yes')