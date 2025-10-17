# 프린터

import sys
from collections import deque

def is_print(case):
    idx, imp = case
    for i in range(1, len(docs_idx)):
        if docs_idx[i][1] > imp:
            return False
    return True

T = int(sys.stdin.readline().strip())
for t in range(T):
    n, m = map(int, sys.stdin.readline().strip().split())
    docs = list(map(int, sys.stdin.readline().strip().split()))
    cnt = 1

    docs_idx = deque()
    for idx, doc in enumerate(docs):
        docs_idx.append((idx, doc))

    # 이번 파일이 내가 찾는 게 아니고 프린트 불가능한 동안
    while not(docs_idx[0][0] == m and is_print(docs_idx[0])):
        if is_print(docs_idx[0]):
            docs_idx.popleft()
            cnt += 1
        else:
            t = docs_idx.popleft()
            docs_idx.append(t)
    print(cnt)
