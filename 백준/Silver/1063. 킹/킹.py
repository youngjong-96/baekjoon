import sys

input = sys.stdin.readline

# 입력 받기
info = input().split()
king_pos = info[0]
stone_pos = info[1]
n = int(info[2])

# 좌표 변환
def to_coord(pos):
    x = ord(pos[0]) - ord('A')
    y = int(pos[1]) - 1
    return [x, y]


# 좌표 역변환
def to_str(pos):
    x_char = chr(pos[0] + ord('A'))
    y_char = str(pos[1] + 1)
    return x_char + y_char

# 현재 위치 설정
k = to_coord(king_pos)
s = to_coord(stone_pos)

# 이동 방향
moves = {
    'R': (1, 0), 'L': (-1, 0),
    'B': (0, -1), 'T': (0, 1),
    'RT': (1, 1), 'LT': (-1, 1),
    'RB': (1, -1), 'LB': (-1, -1)
}

for _ in range(n):
    cmd = input().strip()
    dx, dy = moves[cmd]

    nx = k[0] + dx
    ny = k[1] + dy

    # 체스판 벗어나는지 확인
    if not (0 <= nx < 8 and 0 <= ny < 8):
        continue

    # 돌이랑 겹치는지 확인
    if (nx, ny) == (s[0], s[1]):
        # 돌의 예상 이동 위치
        nsx = s[0] + dx
        nsy = s[1] + dy

        # 돌이 체스판을 벗어나는지 확인
        if not (0 <= nsx < 8 and 0 <= nsy < 8):
            continue  # 돌이 나가면 킹도 이동 안 함

        # 돌 위치 갱신
        s = [nsx, nsy]

    # 킹 위치 갱신
    k = [nx, ny]

# 결과 출력
print(to_str(k))
print(to_str(s))