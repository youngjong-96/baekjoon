import sys
from collections import deque
# sys.stdin = open('sample_input.txt', 'r')
input = sys.stdin.readline

graph = [[] for _ in range(110)]
for i in range(1, 100):
    graph[i].extend([i+1, i+2, i+3, i+4, i+5, i+6])

# 사다리, 뱀 입력받기
teleport = [0] * 110
n, m = map(int, input().split())
for i in range(n+m):
    s, e = map(int, input().split())
    teleport[s] = e

result = 100

def bfs(start):
    global result
    que = deque([start])
    visited = [0] * 110
    visited[start] = 1

    while que:
        t = que.popleft()
        # 100번 칸에 도착했으면 주사위 굴린 횟수를 반환
        if t == 100:
            result = visited[100] - 1
            return

        for next_step in graph[t]:
            destination = next_step

            # 뱀이나 사다리가 있다면 즉시 이동
            if teleport[next_step]:
                destination = teleport[next_step]

            # 목적지가 방문했던 곳인지 확인하고
            # 주사위 횟수를 기록하고 que에 넣는다
            if not visited[destination]:
                visited[destination] = visited[t] + 1
                que.append(destination)

bfs(1)
print(result)