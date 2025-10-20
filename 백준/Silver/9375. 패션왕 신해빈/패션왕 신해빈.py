# 패션왕 신해빈

import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    n = int(sys.stdin.readline().strip())
    data = {}
    # {'headgear': ['hat', 'turban'], 'eyewear': ['sunglasses']}
    for _ in range(n):
        cloth, category = sys.stdin.readline().strip().split()
        data.setdefault(category, []).append(cloth)

    result = 1
    for key in data:
        result *= (len(data[key]) + 1)
        
    print(result - 1)