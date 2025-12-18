import sys

input = sys.stdin.readline

# 입력을 받는 부분
N, JM, HS = map(int, sys.stdin.readline().split())

round_count = 0

while JM != HS:
    # 1. 라운드 수를 1 증가시킵니다.
    round_count += 1

    # 2. 김지민의 다음 라운드 번호를 갱신합니다.
    JM = (JM + 1) // 2

    # 3. 임한수의 다음 라운드 번호를 갱신합니다.
    HS = (HS + 1) // 2

# 4. 두 번호가 같아졌을 때의 라운드를 출력합니다.
print(round_count)