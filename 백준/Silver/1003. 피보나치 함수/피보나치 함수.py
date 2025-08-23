# 피보나치 함수

fibo = [0] * 40
fibo[0] = 1
fibo[1] = 1
for i in range(2,40):
    fibo[i] = fibo[i-2] + fibo[i-1]

T = int(input())

for t in range(T):
    n = int(input())
    if n == 0:
        print('1 0')
    elif n == 1:
        print('0 1')
    else:
        print(fibo[n-2], fibo[n-1])
