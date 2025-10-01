import sys
from collections import deque

def find_2_friends(start_node):
    # visited 배열을 거리 저장용으로 사용. -1은 미방문 상태
    distance = [-1] * n 
    que = deque([(start_node, 0)]) # (노드, 거리)
    distance[start_node] = 0
    
    count = 0
    while que:
        curr_node, dist = que.popleft()
        
        # 거리가 2를 초과하면 더 이상 탐색하지 않음
        if dist >= 2:
            continue
            
        for neighbor in graph[curr_node]:
            if distance[neighbor] == -1: # 아직 방문하지 않은 노드라면
                distance[neighbor] = dist + 1
                que.append((neighbor, dist + 1))
                count += 1
                
    return count

n = int(sys.stdin.readline().strip())
graph = [[] for _ in range(n)]

for i in range(n):
    data = sys.stdin.readline().strip()
    for j in range(n):
        if data[j] == 'Y':
            graph[i].append(j)

result = 0
for i in range(n):
    result = max(result, find_2_friends(i))

print(result)