# 숫자의 개수

number = 1
for _ in range(3):
    n = int(input())
    number *= n

number = list(str(number))

for i in range(10):
    print(number.count(str(i)))