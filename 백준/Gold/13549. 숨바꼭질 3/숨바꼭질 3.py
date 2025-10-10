from collections import deque

n, k = map(int, input().split())

MAX = 100001
visited = [-1] * MAX

def bfs():
    q = deque()
    q.append(n)
    visited[n] = 0

    while q:
        current_pos = q.popleft()

        if current_pos == k:
            return visited[current_pos]

        # 1. 순간이동 (* 2) - 비용 0
        next_pos = current_pos * 2
        if 0 <= next_pos < MAX and visited[next_pos] == -1:
            visited[next_pos] = visited[current_pos] # 비용이 그대로
            q.appendleft(next_pos) # 덱의 앞에 추가

        # 2. 뒤로 걷기 (- 1) - 비용 1
        next_pos = current_pos - 1
        if 0 <= next_pos < MAX and visited[next_pos] == -1:
            visited[next_pos] = visited[current_pos] + 1
            q.append(next_pos) # 덱의 뒤에 추가

        # 3. 앞으로 걷기 (+ 1) - 비용 1
        next_pos = current_pos + 1
        if 0 <= next_pos < MAX and visited[next_pos] == -1:
            visited[next_pos] = visited[current_pos] + 1
            q.append(next_pos) # 덱의 뒤에 추가


# n이 k보다 크거나 같을 경우, 뒤로 걷는 방법밖에 없음
if n >= k:
    print(n - k)
else:
    print(bfs())