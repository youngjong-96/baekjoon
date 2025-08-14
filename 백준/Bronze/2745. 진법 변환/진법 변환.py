# B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.
# 첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36)
# 진법 계산법 : 각 자리 x 진법^자리 위치(?)

n, b = map(str, input().split())
N = len(n)
numbers = ['0','1','2','3','4','5','6','7','8','9']
result = 0

for i in range(N-1,-1,-1):
    if n[i] in numbers:
        result += int(n[i]) * (int(b) ** (N-i-1))
    else:
        result += (ord(n[i])-55) * (int(b) ** (N-i-1))

print(result)

