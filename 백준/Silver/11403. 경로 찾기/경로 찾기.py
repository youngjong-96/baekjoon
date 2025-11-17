import sys
from collections import deque

# 경로가 있는지 확인하는 함수
def find_route(start, target):
    # queue 선언 후 초기값으로 시작하는 노드의 인접 노드들 전달
    que = deque([start])
    visited = [0] * n
    visited[start] = 1

    while que:
        node = que.popleft()
        # 노드를 순회하며 노드가 찾으려는 도착지와 같으면 1 리턴
        # 없으면 인접 노드들 queue에 append
        for next_node in graph_lst[node]:
            if next_node == target:
                return 1

            if not visited[next_node]:
                visited[next_node] = 1
                que.append(next_node)
    return 0


n = int(sys.stdin.readline().strip())
# 초기 그래프(인접 행렬)
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

# 그래프(인접 리스트)
graph_lst = [[] for _ in range(n)]

# 그래프 인접 리스트로 변환
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            graph_lst[i].append(j)

# 각 노드들에 대해서 갈 수 있는 경로가 있는지 확인 후 결과 출력
for i in range(n):
    for j in range(n):
        if find_route(i, j):
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()