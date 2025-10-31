import sys

# p: 초기 피로도, n: 장신구 개수
p, n = map(int, sys.stdin.readline().strip().split())

# cost: 각 장신구 제작 비용
cost = list(map(int, sys.stdin.readline().strip().split()))

cost.sort()

count = 0 # 만든 장신구 개수

# 비용이 적은 것부터 순서대로 확인
for i in range(n):
    # 현재 피로도가 200 미만이어야만 제작 가능
    if p < 200:
        p += cost[i]  # 장신구 제작 (피로도 증가)
        count += 1    # 개수 증가
    else:
        # 피로도가 200 이상이면 더 이상 만들 수 없으므로 중단
        break

# 최종 개수 출력
print(count)