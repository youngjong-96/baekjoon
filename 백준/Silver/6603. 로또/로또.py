import sys
from itertools import combinations

input = sys.stdin.readline

while True:
    S = list(map(int, input().split()))
    if S == [0]:
        break
    
    S = S[1:]
    S_set = set(S)
    S = list(S_set)
    S.sort()

    
    result = combinations(S, 6)
    for case in result:
        print(*case)
    print()