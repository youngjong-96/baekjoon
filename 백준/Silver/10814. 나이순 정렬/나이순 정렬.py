# 나이순 정렬

"""
온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다.
이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.
"""

import sys

n = int(sys.stdin.readline().strip())

data = []
for _ in range(n):
    age, name = sys.stdin.readline().strip().split()
    data.append((age, name))

data.sort(key=lambda x : int(x[0]))

for age, name in data:
    print(age, name)