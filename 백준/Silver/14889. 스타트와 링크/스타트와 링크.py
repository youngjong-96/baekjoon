import sys
from itertools import combinations


input = sys.stdin.readline

N = int(input().strip())
data = [list(map(int, input().split())) for _ in range(N)]

all_members = set(range(N))  # 0부터 N-1까지의 인덱스 사용
result = float('inf')

# 1. 전체 인원 중 절반(N//2)을 뽑아 스타트 팀(team_A)을 구성
for team_A in combinations(range(N), N // 2):
    team_B = list(all_members - set(team_A)) # 나머지는 자동으로 링크 팀
    
    # 2. 각 팀의 능력치 계산
    score_A = 0
    score_B = 0
    
    # 팀 내에서 2명씩 뽑아 시너지 합산
    for i, j in combinations(team_A, 2):
        score_A += data[i][j] + data[j][i]
        
    for i, j in combinations(team_B, 2):
        score_B += data[i][j] + data[j][i]
    
    # 3. 최솟값 갱신
    result = min(result, abs(score_A - score_B))
    
    if result == 0:
        break

print(result)