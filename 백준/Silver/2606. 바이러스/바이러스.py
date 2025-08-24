# 바이러스

"""
1번 컴퓨터와 연결된 컴퓨터는 모두 바이러스에 감염
감염되는 컴퓨터 수를 구하여라
"""
from collections import deque

# 첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하인 양의 정수이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다.
c = int(input())

# 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.
n = int(input())

network = [[] for _ in range(c + 1)]

for i in range(n):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

visited = []
q = deque()
q.append(1)
visited.append(1)

while q:
    t = q.popleft()

    for com in network[t]:
        if com not in visited:
            q.append(com)
            visited.append(com)

print(len(visited) - 1)