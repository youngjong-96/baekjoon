# 구간합

"""
1. n 개의 정수가 들어있는 배열에서 이웃한 m 개의 합 중 최대값과 최소값의 차이를 출력
"""
"""
최악 n = 100, m = 2인 경우 연산 99번 -> 완탐 ssap possible
"""

# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
T = int(input())
for t in range(1, T+1):
    # 다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )
    n, m = map(int, input().split())

    # 다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )
    numbers = list(map(int, input().split()))

    min_sum = 10e19
    max_sum = 0

    for i in range(n-m+1):
        total = sum(numbers[i:i+m])
        min_sum = min(min_sum, total)
        max_sum = max(max_sum, total)

    print(f'#{t} {max_sum - min_sum}')