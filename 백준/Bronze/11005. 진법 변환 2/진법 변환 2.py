# 진법 변환 2

# 10진법 수 N을 B진법으로 바꾸어서 출력하는 프로그램을 작성하시오


# 첫째 줄에 N과 B가 주어진다
n, b = map(int, input().split())

data = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# 더 이상 나누어 지지 않을 때까지 n 을 b 로 계속 나눈다
# 나머지는 따로 저장하고 마지막 몫부터 역순으로 출력한다 -> stack 이용
# 만들어진 리스트를 data 에 대응하여 출력한다 -> index 이용

stack = []
result = ''
if n == 0: result = 0

while n > 0:
    stack.append(n % b)
    n = n//b

while stack:
    result += data[stack.pop()]

print(result)