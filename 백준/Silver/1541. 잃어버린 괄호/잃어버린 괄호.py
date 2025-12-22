import sys
# '-'로 나누고, 각 부분을 '+'로 나눠 합친 리스트 생성
parts = [sum(map(int, x.split('+'))) for x in sys.stdin.readline().split('-')]
# 첫 번째 값에서 나머지를 전부 차감
print(parts[0] - sum(parts[1:]))