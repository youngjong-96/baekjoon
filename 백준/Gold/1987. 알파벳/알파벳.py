import sys

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def solve():
    R, C = map(int, input().split())
    board = [input().strip() for _ in range(R)]

    queue = set([(0, 0, board[0][0])])
    max_dist = 1

    while queue:
        r, c, path = queue.pop()
        max_dist = max(max_dist, len(path))

        if max_dist == 26:
            break

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < R and 0 <= nc < C:
                if board[nr][nc] not in path:
                    queue.add((nr, nc, path + board[nr][nc]))

    print(max_dist)

solve()