import sys
from collections import Counter

input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    data = list(map(int, input().split()))
    t = data[0]
    data = data[1:]

    # data 리스트의 각 요소 개수를 즉시 계산
    counts = Counter(data)

    # 가장 많이 등장한 요소와 그 횟수 가져오기
    most_common_id, max_count = counts.most_common(1)[0]
    
    if max_count > t//2:
        print(most_common_id)
    else:
        print('SYJKGW')