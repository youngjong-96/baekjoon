import sys

# sys.stdin = open('sample_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
target = int(input())

result = [[0] * n for _ in range(n)]
x = n // 2
y = n // 2

result[x][y] = 1  # 중앙값 1 채우기

# 방향: 위 -> 오른쪽 -> 아래 -> 왼쪽
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# 처음에 위를 보고 시작
dir_idx = 0
ans_x, ans_y = x + 1, y + 1

# 2부터 채우기 시작
for next_num in range(2, n * n + 1):
    # 1. [선 이동] 일단 현재 방향으로 한 칸 이동해서 숫자를 채웁니다.
    x += di[dir_idx]
    y += dj[dir_idx]
    result[x][y] = next_num

    if next_num == target:
        ans_x, ans_y = x + 1, y + 1

    # 2. [후 판단] 현재 위치에서 '오른쪽(다음 방향)'을 봅니다.
    next_dir = (dir_idx + 1) % 4
    nx = x + di[next_dir]
    ny = y + dj[next_dir]

    # 오른쪽 칸이 비어있다면(0이라면) 방향을 틀어줍니다.
    # (이미 숫자가 있다면 방향을 유지합니다)
    if result[nx][ny] == 0:
        dir_idx = next_dir

# 1이 target일 경우 예외 처리
if target == 1:
    ans_x, ans_y = n // 2 + 1, n // 2 + 1

for row in result:
    print(' '.join(map(str, row)))
print(ans_x, ans_y)