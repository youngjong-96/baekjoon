# 구간 합 구하기 4
"""
수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.
"""

import sys
# 첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다.
n, m = map(int, sys.stdin.readline().strip().split())
# 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다.
numbers = list(map(int, sys.stdin.readline().strip().split()))
# 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.
numbers_sum = [0] * n
numbers_sum[0] = numbers[0]

for i in range(1, len(numbers)):
    numbers_sum[i] = numbers_sum[i-1] + numbers[i]


for _ in range(m):
    i, j = map(int, sys.stdin.readline().strip().split())
    if i == 1:
        print(numbers_sum[j-1])
    else:
        print(numbers_sum[j-1] - numbers_sum[i-2])
