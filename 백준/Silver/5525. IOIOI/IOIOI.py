import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
S = sys.stdin.readline().strip()

answer = 0       # 최종 Pn 개수
pattern_count = 0  # 연속된 "IOI" 패턴의 개수
i = 0

while i < (m - 2):
    if S[i] == 'I' and S[i+1] == 'O' and S[i+2] == 'I':
        pattern_count += 1
        i += 2  # 'I'O'I' 다음 'O'I'를 확인하기 위해 2칸 점프
        
        # 만약 pattern_count가 N과 같아졌다면, Pn을 하나 찾은 것
        if pattern_count == n:
            answer += 1
            pattern_count -= 1 
            
    else:
        # "IOI" 패턴이 깨진 경우
        pattern_count = 0  # 카운트 리셋
        i += 1  # 다음 칸부터 다시 탐색

print(answer)