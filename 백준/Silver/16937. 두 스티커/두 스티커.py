import sys


# 종이 세로, 가로
H, W = map(int, sys.stdin.readline().strip().split())
# 스티커의 수
N = int(sys.stdin.readline().strip())
stickers = []

# sticker들 입력받기(못 쓰는건 버리기)  O(n)
for i in range(N):
    R, C = map(int, sys.stdin.readline().strip().split())
    if (R <= H or R <= W) and (C <= H or C <= W):
        stickers.append((R, C))

result = 0

def check(lst):
    s1, s2 = lst

    if s1[0] + s2[0] <= W and s1[1] <= H and s2[1] <= H:
        return True
    if s1[0] + s2[1] <= W and s1[1] <= H and s2[0] <= H:
        return True
    if s1[1] + s2[0] <= W and s1[0] <= H and s2[1] <= H:
        return True
    if s1[1] + s2[1] <= W and s1[0] <= H and s2[0] <= H:
        return True

    if s1[0] + s2[0] <= H and s1[1] <= W and s2[1] <= W:
        return True
    if s1[0] + s2[1] <= H and s1[1] <= W and s2[0] <= W:
        return True
    if s1[1] + s2[0] <= H and s1[0] <= W and s2[1] <= W:
        return True
    if s1[1] + s2[1] <= H and s1[0] <= W and s2[0] <= W:
        return True



def recur(idx, lst):
    global result

    # 종료조건: 2개를 고르면 조건에 맞는지 확인하고 최대값 갱신
    if len(lst) >= 2:
        if(check(lst)):
            s1, s2 = lst
            result = max(result, (s1[0] * s1[1]) + (s2[0] * s2[1]))
            return
        else:
            return

    if idx >= len(stickers):
        return

    # 스티커가 서로 달라서 고른 경우
    recur(idx + 1, lst + [stickers[idx]])

    # 지금 스티커를 안 고른 경우
    recur(idx + 1, lst)


recur(0, [])

print(result)
