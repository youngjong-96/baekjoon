# 나무 자르기

import sys

# 현제 기준에서 획득 가능한 나무 길이를 반환하는 함수
def cnt(std):
    value = 0
    for tree in trees:
        if tree > std:
            value += tree - std
    return value

# n = 나무수, m = 필요 길이
n, m = map(int, sys.stdin.readline().strip().split())
trees = list(map(int, sys.stdin.readline().strip().split()))

m_tree = max(trees) # 가장 긴 나무
s = 0 # 최소 높이

result = 0  # 결과(적어도 m 미터의 나무를 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값)

#
while m_tree - s != 1:
    mid = (m_tree + s) // 2
    # 조건을 만족하면 더 높은 높이에서 만족할 수 없는지 확인한다
    if cnt(mid) >= m:
        s = mid
        # 조건을 만족하고 mid가 현재 result 보다 크다면 교체
        if result < mid:
            result = mid
    # 조건을 만족하지 않으면 기준 높이를 더 낮춘다
    elif cnt(mid) < m:
        m_tree = mid

print(result)