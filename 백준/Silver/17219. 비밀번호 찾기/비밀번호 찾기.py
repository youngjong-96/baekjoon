# 비밀번호 찾기

import sys

# n = 저장된 사이트 수, m = 찾으려는 사이트 수
n, m = map(int, sys.stdin.readline().strip().split())

data = {}

for _ in range(n):
    site, password = sys.stdin.readline().strip().split()
    data.setdefault(site, password)

for _ in range(m):
    find = sys.stdin.readline().strip()
    print(data[find])