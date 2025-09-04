# n과 m2

"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
고른 수열은 오름차순이어야 한다.
"""

import sys


n, m = map(int, sys.stdin.readline().strip().split())

def recur(start):
    if len(path) == m:
        print(*path)

    for i in range(start, n+1):   # 1. 후보군의 시작이 start 부터 라는 것
        path.append(i)
        recur(i + 1)    # 2. i 다음부터 탐색한다는 것
        path.pop()

path = []
recur(1)  # 3. 1부터 시작한다는 것

