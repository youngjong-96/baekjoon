# 약수 구하기

"""
두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성하시오.
"""

n, k = map(int, input().split())

for i in range(1, n+1):
    if n % i == 0:
        k -= 1
        if k == 0:
            result = i
            break

if k != 0:
    result = 0


print(result)