import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

old_warehouses = [int(input()) for _ in range(n)]
new_warehouses = [int(input()) for _ in range(m)]


total_old = sum(old_warehouses)
total_new = sum(new_warehouses)
total_move = min(total_old, total_new)


ans_count = total_move
ans_cost = 0

# 기존 창고에서 짐 빼기 (비용 계산)
temp_move = total_move
for i in range(n):
    if temp_move <= 0:
        break
    
    # 현재 창고에서 뺄 수 있는 양 계산
    take = min(old_warehouses[i], temp_move)
    ans_cost += take * (i + 1) 
    temp_move -= take

# 새 창고에 짐 넣기
temp_move = total_move
for i in range(m):
    if temp_move <= 0:
        break
    
    # 현재 창고에 넣을 수 있는 양 계산
    put = min(new_warehouses[i], temp_move)
    ans_cost += put * (i + 1)
    temp_move -= put

print(f"{ans_count} {ans_cost}")