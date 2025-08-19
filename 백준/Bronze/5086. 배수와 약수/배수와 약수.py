# 약수와 배수

"""
1. 첫 번째 숫자가 두 번째 숫자의 약수라면 factor
2. 첫 번째 숫자가 두 번째 숫자의 배수라면 multiple
3. 둘 다 아니라면 neither
4. 0 0 이 입력되면 종료
"""

a, b = 1, 1
while True:
    a, b = map(int, input().split())

    if b != 0 and b % a == 0:
        result = 'factor'
    elif a != 0 and a % b == 0:
        result = 'multiple'
    elif a == 0 and b == 0:
        break
    else:
        result = 'neither'

    print(result)