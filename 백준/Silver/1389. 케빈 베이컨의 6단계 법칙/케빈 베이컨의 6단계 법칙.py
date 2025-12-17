import sys
from collections import deque
#sys.stdin = open('sample_input.txt', 'r')
input = sys.stdin.readline

# n:유저수, m:친구 관계 수
n, m = map(int, input().split())

# idx 0번 사용 x
graph = [set() for _ in range(n+1)]

# 그래프 입력 받기
# [set(), {3, 4}, {3}, {1, 2, 4}, {1, 3, 5}, {4}]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

def find_friend(start):
    que = deque([start])
    visited = [-1] * (n + 1)
    visited[start] = 0

    while que:
        node = que.popleft()
        for next_node in graph[node]:
            # 방문하지 않은 곳이라면
            if visited[next_node] == -1:
                # 이전 노드의 거리 + 1을 저장
                visited[next_node] = visited[node] + 1
                que.append(next_node)
            # start 노드에서 모든 노드까지의 거리 합을 반환
    return sum(visited[1:])

result = []
for i in range(1, n+1):
    result.append(find_friend(i))

print(result.index(min(result)) + 1)