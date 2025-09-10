# 회의실 배정
import sys

# 회의 개수
n = int(sys.stdin.readline().strip())

# 회의 시작시간, 끝나는 시간 정보
data = []
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().strip().split())))

# 끝나는 시간 기준 정렬
data.sort(key=lambda x: (x[1], x[0]))

if not data:
    print(0)
else:
    # 첫 번째 끝나는 시간 기준
    std = data[0][1]

    # 첫번째 회의 시작
    result = 1

    # 시작 시간이 기준보다 같거나 뒤이면 회의 가능
    for s, e in data[1:]:
        if s >= std:
            result += 1
            # 끝나는 시간 변경
            std = e
    
    print(result)