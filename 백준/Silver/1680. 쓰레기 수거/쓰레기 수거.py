import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    W, N = map(int, input().split())
    data = []
    for _ in range(N):
        data.append(list(map(int, input().split())))

    result = 0
    car_weight = 0
    curr_pos = 0  # 현재 트럭의 위치를 추적

    for i in range(N):
        x, w = data[i]
        
        # 1. 현재 지점까지 이동 (직전 위치가 0이든 이전 지점이든 상관없음)
        result += (x - curr_pos)
        curr_pos = x
        
        # 2. 수거 조건 체크
        if car_weight + w < W:
            # 여유가 있으면 싣고 끝
            car_weight += w
        elif car_weight + w == W:
            # 딱 맞으면 싣고 쓰레기장으로 복귀
            result += x
            car_weight = 0
            curr_pos = 0  # 트럭 위치 초기화
        else:
            # 용량이 부족하면 쓰레기장 갔다와서 수거
            result += (x * 2)
            car_weight = w
            curr_pos = x  # 다시 현재 위치 x로 돌아옴

    # 3. 모든 지점 방문 후 아직 쓰레기장에 돌아가지 않았다면 마지막 복귀
    if curr_pos != 0:
        result += curr_pos

    print(result)