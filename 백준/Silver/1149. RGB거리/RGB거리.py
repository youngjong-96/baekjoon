import sys

input = sys.stdin.readline

n = int(input().strip())
costs = [list(map(int, input().strip().split())) for _ in range(n)]

# costs[i][0]: R, costs[i][1]: G, costs[i][2]: B
# costs를 dp 테이블로 그대로 사용
# 0번 인덱스(첫 집)는 비용 그대로 시작
for i in range(1, n):
    # i번째 집을 빨강(0)으로 칠할 경우: 이전 집은 초록(1) 또는 파랑(2) 중 싼 것
    costs[i][0] += min(costs[i-1][1], costs[i-1][2])
    
    # i번째 집을 초록(1)으로 칠할 경우: 이전 집은 빨강(0) 또는 파랑(2) 중 싼 것
    costs[i][1] += min(costs[i-1][0], costs[i-1][2])
    
    # i번째 집을 파랑(2)으로 칠할 경우: 이전 집은 빨강(0) 또는 초록(1) 중 싼 것
    costs[i][2] += min(costs[i-1][0], costs[i-1][1])

print(min(costs[n-1]))

"""
# 백트래킹 시간초과
import sys
sys.stdin = open('input.txt', 'r')

def recur(idx, color, cost):
    global result
    # 종료조건
    if len(pick) == n:
        if result > cost:
            result = cost
        return
    
    for i in range(3):
        if color == i:
            continue
        pick.append(i)
        recur(idx + 1, i, cost + costs[idx][i])
        pick.pop()
        

n = int(sys.stdin.readline().strip())
costs = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

pick = []
result = float('inf')

recur(0, 4, 0)
print(result)
"""